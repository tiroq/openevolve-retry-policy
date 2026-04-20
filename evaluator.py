"""Evaluator for OpenEvolve retry/backoff policy evolution.

This file can be used both by OpenEvolve and directly from the CLI.
The key contract is that evaluation must produce a `combined_score`.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import statistics
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, List

from scenarios import Scenario, build_holdout_scenarios, build_train_scenarios


NON_RETRYABLE_ERRORS = {"invalid_request"}


@dataclass
class StepResult:
    success: bool
    total_latency_ms: int
    retries: int
    dangerous_non_idempotent_retries: int
    useless_retries: int
    good_fail_fast: int
    good_switch: int
    actions: List[Dict[str, int | str]]


@dataclass
class EvalResult:
    metrics: Dict[str, float]
    scenario_results: List[StepResult]


ChooseAction = Callable[[int, str, int, int, int, bool, bool], Dict[str, int | str]]


def load_program(program_path: str) -> tuple[ChooseAction, Callable[[Dict[str, int | str]], Dict[str, int | str]]]:
    path = Path(program_path)
    spec = importlib.util.spec_from_file_location("candidate_program", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load program from {program_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    choose_action = getattr(module, "choose_action", None)
    normalize_action = getattr(module, "normalize_action", None)
    if choose_action is None or normalize_action is None:
        raise RuntimeError("Program must define choose_action and normalize_action")
    return choose_action, normalize_action


def scenario_would_succeed_without_switch(s: Scenario, attempt: int, elapsed_ms: int) -> bool:
    if s.error_type in NON_RETRYABLE_ERRORS:
        return False
    if s.recovery_attempt is not None and attempt >= s.recovery_attempt:
        return True
    if s.recovery_after_elapsed_ms is not None and elapsed_ms >= s.recovery_after_elapsed_ms:
        return True
    return False


def scenario_would_succeed_with_switch(s: Scenario) -> bool:
    return s.primary_endpoint_bad_until_attempt == 99


def run_scenario(
    scenario: Scenario,
    choose_action: ChooseAction,
    normalize_action: Callable[[Dict[str, int | str]], Dict[str, int | str]],
) -> StepResult:
    elapsed_ms = 0
    retries = 0
    consecutive_failures = 0
    dangerous_non_idempotent_retries = 0
    useless_retries = 0
    good_fail_fast = 0
    good_switch = 0
    circuit_open = False
    last_rtt_ms = scenario.latency_ms
    on_primary_endpoint = True
    actions: List[Dict[str, int | str]] = []

    for attempt in range(scenario.max_attempts):
        if on_primary_endpoint and scenario.primary_endpoint_bad_until_attempt == 99:
            endpoint_success_possible = False
        else:
            endpoint_success_possible = True

        if endpoint_success_possible and scenario_would_succeed_without_switch(scenario, attempt + 1, elapsed_ms):
            return StepResult(
                success=True,
                total_latency_ms=elapsed_ms + scenario.latency_ms,
                retries=retries,
                dangerous_non_idempotent_retries=dangerous_non_idempotent_retries,
                useless_retries=useless_retries,
                good_fail_fast=good_fail_fast,
                good_switch=good_switch,
                actions=actions,
            )

        raw = choose_action(
            attempt,
            scenario.error_type,
            elapsed_ms,
            last_rtt_ms,
            consecutive_failures,
            scenario.is_idempotent,
            circuit_open,
        )
        decision = normalize_action(raw)
        actions.append(decision)
        action = decision["action"]
        wait_ms = int(decision["wait_ms"])

        if action == "fail":
            if scenario.error_type in NON_RETRYABLE_ERRORS:
                good_fail_fast += 1
            elif not scenario.is_idempotent and attempt >= 1:
                good_fail_fast += 1
            elif scenario.recovery_attempt is None and scenario.recovery_after_elapsed_ms is None and scenario.primary_endpoint_bad_until_attempt is None:
                good_fail_fast += 1
            return StepResult(
                success=False,
                total_latency_ms=elapsed_ms,
                retries=retries,
                dangerous_non_idempotent_retries=dangerous_non_idempotent_retries,
                useless_retries=useless_retries,
                good_fail_fast=good_fail_fast,
                good_switch=good_switch,
                actions=actions,
            )

        if action == "open_circuit":
            circuit_open = True
            return StepResult(
                success=False,
                total_latency_ms=elapsed_ms + wait_ms,
                retries=retries,
                dangerous_non_idempotent_retries=dangerous_non_idempotent_retries,
                useless_retries=useless_retries,
                good_fail_fast=good_fail_fast + 1,
                good_switch=good_switch,
                actions=actions,
            )

        if action == "switch_endpoint":
            on_primary_endpoint = False
            elapsed_ms += wait_ms
            retries += 1
            consecutive_failures += 1
            if scenario_would_succeed_with_switch(scenario):
                good_switch += 1
                return StepResult(
                    success=True,
                    total_latency_ms=elapsed_ms + scenario.latency_ms,
                    retries=retries,
                    dangerous_non_idempotent_retries=dangerous_non_idempotent_retries,
                    useless_retries=useless_retries,
                    good_fail_fast=good_fail_fast,
                    good_switch=good_switch,
                    actions=actions,
                )
            useless_retries += 1
            continue

        if action == "retry":
            retries += 1
            consecutive_failures += 1
            elapsed_ms += wait_ms + scenario.latency_ms
            if not scenario.is_idempotent and attempt >= 1:
                dangerous_non_idempotent_retries += 1
            if scenario.recovery_attempt is None and scenario.recovery_after_elapsed_ms is None and scenario.primary_endpoint_bad_until_attempt is None:
                useless_retries += 1
            continue

        # Defensive fallback: unknown action should be treated as fail.
        return StepResult(
            success=False,
            total_latency_ms=elapsed_ms,
            retries=retries,
            dangerous_non_idempotent_retries=dangerous_non_idempotent_retries,
            useless_retries=useless_retries + 1,
            good_fail_fast=good_fail_fast,
            good_switch=good_switch,
            actions=actions,
        )

    return StepResult(
        success=False,
        total_latency_ms=elapsed_ms,
        retries=retries,
        dangerous_non_idempotent_retries=dangerous_non_idempotent_retries,
        useless_retries=useless_retries,
        good_fail_fast=good_fail_fast,
        good_switch=good_switch,
        actions=actions,
    )


def aggregate(results: List[StepResult]) -> Dict[str, float]:
    successes = [1.0 if r.success else 0.0 for r in results]
    latencies = [float(r.total_latency_ms) for r in results]
    retries = [float(r.retries) for r in results]
    dangerous = [float(r.dangerous_non_idempotent_retries) for r in results]
    useless = [float(r.useless_retries) for r in results]
    fail_fast = [float(r.good_fail_fast) for r in results]
    good_switch = [float(r.good_switch) for r in results]

    success_rate = statistics.mean(successes)
    avg_latency_ms = statistics.mean(latencies)
    avg_retry_count = statistics.mean(retries)
    dangerous_non_idempotent_retries = statistics.mean(dangerous)
    useless_retries = statistics.mean(useless)
    good_fail_fast_decisions = statistics.mean(fail_fast)
    good_endpoint_switches = statistics.mean(good_switch)

    combined_score = (
        100.0 * success_rate
        - 0.03 * avg_latency_ms
        - 2.5 * avg_retry_count
        - 25.0 * dangerous_non_idempotent_retries
        - 10.0 * useless_retries
        + 8.0 * good_fail_fast_decisions
        + 5.0 * good_endpoint_switches
    )

    return {
        "runs_successfully": 1.0,
        "success_rate": round(success_rate, 6),
        "avg_latency_ms": round(avg_latency_ms, 6),
        "avg_retry_count": round(avg_retry_count, 6),
        "dangerous_non_idempotent_retries": round(dangerous_non_idempotent_retries, 6),
        "useless_retries": round(useless_retries, 6),
        "good_fail_fast_decisions": round(good_fail_fast_decisions, 6),
        "good_endpoint_switches": round(good_endpoint_switches, 6),
        "combined_score": round(combined_score, 6),
    }


def evaluate_program(program_path: str, dataset: str = "train") -> EvalResult:
    choose_action, normalize_action = load_program(program_path)
    if dataset == "train":
        scenarios = build_train_scenarios()
    elif dataset == "holdout":
        scenarios = build_holdout_scenarios()
    else:
        raise ValueError(f"Unknown dataset: {dataset}")

    results = [run_scenario(s, choose_action, normalize_action) for s in scenarios]
    metrics = aggregate(results)
    return EvalResult(metrics=metrics, scenario_results=results)


def evaluate(program_path: str) -> Dict[str, float]:
    """OpenEvolve-compatible entrypoint.

    OpenEvolve examples optimize `combined_score`. This function returns a metric
    dictionary in the same spirit.
    """
    return evaluate_program(program_path=program_path, dataset="train").metrics


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--program", required=True, help="Path to candidate program")
    parser.add_argument("--dataset", choices=["train", "holdout"], default="train")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        result = evaluate_program(program_path=args.program, dataset=args.dataset)
        if args.json:
            print(json.dumps(result.metrics, indent=2, sort_keys=True))
        else:
            for key, value in result.metrics.items():
                print(f"{key}: {value}")
        return 0
    except Exception:
        failure = {
            "runs_successfully": 0.0,
            "success_rate": 0.0,
            "avg_latency_ms": 999999.0,
            "avg_retry_count": 999.0,
            "dangerous_non_idempotent_retries": 999.0,
            "useless_retries": 999.0,
            "good_fail_fast_decisions": 0.0,
            "good_endpoint_switches": 0.0,
            "combined_score": -1e9,
            "traceback": traceback.format_exc(),
        }
        if args.json:
            print(json.dumps(failure, indent=2, sort_keys=True))
        else:
            print(failure["traceback"])
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
