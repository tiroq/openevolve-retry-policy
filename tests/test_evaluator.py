from evaluator import evaluate, evaluate_program, run_scenario
from scenarios import Scenario
from initial_program import normalize_action


def test_evaluator_returns_combined_score():
    result = evaluate_program("initial_program.py", dataset="train")
    assert "combined_score" in result.metrics
    assert result.metrics["runs_successfully"] == 1.0


def test_holdout_evaluation_runs():
    result = evaluate_program("initial_program.py", dataset="holdout")
    assert result.metrics["runs_successfully"] == 1.0
    assert result.metrics["avg_latency_ms"] >= 0


def test_evaluate_entrypoint_returns_failure_on_bad_program(tmp_path):
    bad_prog = tmp_path / "bad.py"
    bad_prog.write_text("raise RuntimeError('boom')")
    metrics = evaluate(str(bad_prog))
    assert metrics["combined_score"] == -1e9
    assert metrics["runs_successfully"] == 0.0


def test_evaluate_entrypoint_succeeds_on_valid_program():
    metrics = evaluate("initial_program.py")
    assert metrics["runs_successfully"] == 1.0
    assert "combined_score" in metrics


def test_switch_endpoint_penalizes_non_idempotent():
    scenario = Scenario(
        name="non_idem_switch",
        error_type="timeout",
        is_idempotent=False,
        max_attempts=3,
        recovery_attempt=None,
        recovery_after_elapsed_ms=None,
        primary_endpoint_bad_until_attempt=99,
        latency_ms=100,
        duplicate_risk=1.0,
        description="Switching on non-idempotent after attempt 0 is dangerous.",
    )

    def always_switch(attempt, error_type, elapsed_ms, last_rtt_ms,
                      consecutive_failures, is_idempotent, circuit_open):
        return {"action": "switch_endpoint", "wait_ms": 0}

    result = run_scenario(scenario, always_switch, normalize_action)
    assert result.dangerous_non_idempotent_retries == 0  # attempt 0 is allowed
    # The switch on attempt 0 succeeds, so only 1 action taken
