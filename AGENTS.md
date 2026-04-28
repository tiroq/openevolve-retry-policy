# Project Guidelines
## Overview
This repository is an evaluation-first OpenEvolve case study.
It demonstrates how AI-assisted program evolution can be applied to a realistic QA/reliability problem: evolving a retry/backoff policy for unstable HTTP-style integrations.
The evolved artifact is intentionally small: a single `choose_action()` function inside an `EVOLVE-BLOCK` in `initial_program.py`.
The important artifact is not only the policy itself, but the complete evaluation loop:
- deterministic train and holdout scenario generation;
- measurable reliability, latency, retry, and safety metrics;
- regression visibility between train and holdout;
- repeatable local-model and cloud-model experiment runs;
- documentation of what improved, what regressed, and why.
This repository should be treated as a portfolio-grade example of building evaluation-first AI systems for QA automation, reliability testing, and complex workflow validation.
## Build and Test
Create environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Run tests:

pytest -q

Or use Taskfile:

task lint
task test
task eval

Evaluate baseline locally:

python evaluator.py --program initial_program.py --dataset train --json
python evaluator.py --program initial_program.py --dataset holdout --json

Evaluate a candidate program:

python evaluator.py --program experiments/rounds/round_1_cloud_openevolve_output/best/best_program.py --dataset holdout --json

Or with Taskfile if CANDIDATE is supported:

CANDIDATE=experiments/rounds/round_1_cloud_openevolve_output/best/best_program.py task eval:holdout

Architecture

initial_program.py  -> choose_action() + normalize_action()
evaluator.py        -> dynamic program loading, scenario execution, metric scoring
scenarios.py        -> deterministic train / holdout scenario generation
config.yaml         -> OpenEvolve run configuration for local/OpenAI-compatible models
tests/              -> evaluator, scenario, contract, and regression tests
experiments/rounds/ -> saved OpenEvolve outputs and candidate artifacts
docs/               -> reports, prompts, analysis, and supporting documentation

Core files

* initial_program.py contains the policy being evolved.
* evaluator.py exposes evaluate(program_path) -> Dict[str, float] for OpenEvolve and a CLI with --program, --dataset, and --json.
* scenarios.py creates deterministic scenario sets for training and holdout evaluation.
* config.yaml defines local/OpenAI-compatible model settings for OpenEvolve.
* tests/ protects the evaluator contract and prevents silent breakage.

OpenEvolve Contract

initial_program.py must contain exactly one evolve region:

# EVOLVE-BLOCK-START
...
# EVOLVE-BLOCK-END

Only code inside the evolve block should be mutated.

Everything outside the block is stable infrastructure:

* imports;
* constants;
* allowed action definitions;
* normalize_action();
* public function signature.

The evolved function must preserve this signature:

def choose_action(
    attempt: int,
    error_type: str,
    elapsed_ms: int,
    last_rtt_ms: int,
    consecutive_failures: int,
    is_idempotent: bool,
    circuit_open: bool,
) -> Dict[str, int | str]:
    ...

The function must return:

{"action": str, "wait_ms": int}

Allowed actions:

retry
fail
switch_endpoint
open_circuit

normalize_action() is a safety net. It validates the action and clamps wait_ms to [0, 30000], but evolved code should still return correct values directly.

Evaluation Contract

The evaluator must be deterministic, explicit, and failure-safe.

evaluator.py must expose:

evaluate(program_path) -> Dict[str, float]

The returned dictionary must include float-compatible metrics such as:

* runs_successfully
* success_rate
* avg_latency_ms
* avg_retry_count
* dangerous_non_idempotent_retries
* useless_retries
* good_fail_fast_decisions
* good_endpoint_switches
* combined_score

The primary optimization target is:

combined_score

On any exception, the evaluator must return a hard failure result:

combined_score = -1e9
runs_successfully = 0.0

The evaluator should not crash silently. Failures must be visible through metrics.

Scenario Model

Scenarios simulate unstable HTTP-style integrations where retry behavior can help or harm.

Important scenario concepts:

* recovery_attempt: the failed request may recover after a certain retry attempt.
* recovery_after_elapsed_ms: the integration may recover after enough elapsed time.
* primary_endpoint_bad_until_attempt == 99: sentinel meaning the primary endpoint does not recover soon; endpoint switch is expected.
* non-idempotent requests are dangerous to retry after attempt 0.
* unrecoverable scenarios should usually fail fast instead of wasting retries.

Scenario generation is deterministic for fixed seeds.

Do not break seed-dependent reproducibility.

Current convention:

train seed   = 42
holdout seed = 314

Key Pitfalls

1. Reward hacking

A candidate may improve train combined_score by reducing latency while damaging success rate or holdout behavior.

Do not treat train improvement as final proof.

Always compare:

task eval:train
task eval:holdout

2. Non-idempotent retry violations

Retrying a non-idempotent request after attempt 0 incurs a heavy penalty.

Policies must guard this explicitly.

3. Overfitting to train scenarios

The train set is useful for evolution, but the holdout set is the credibility check.

A candidate that improves train and regresses holdout must be documented as a regression, not promoted as a reliable improvement.

4. Invalid output shape

Local models may produce malformed rewrites, wrong return keys, renamed functions, extra prose, or broken syntax.

The function must preserve:

{"action": ..., "wait_ms": ...}

Not:

{"wait_time": ...}

Not a new helper-only implementation.

Not a renamed function.

5. Mutating stable code

Do not mutate constants, imports, evaluator logic, or scenario generation unless the task explicitly asks for evaluator/framework changes.

For OpenEvolve runs, only the EVOLVE-BLOCK is expected to change.

Documentation Standards

This project is a case study, not just a toy example.

Documentation should explain:

* what was evaluated;
* why the metric exists;
* what improved;
* what regressed;
* what was reproducible;
* what was only observed manually;
* what remains unsafe for production.

Do not hide negative results. Failed model runs, malformed generations, train/holdout regression, and local-model limitations are part of the case study.

Recommended docs:

* README.md — main case study entry point.
* EXPERIMENTS.md — experiment summary and model/run comparison.
* LESSONS_LEARNED.md — technical conclusions and failure modes.
* experiments/README.md — artifact index.
* docs/reports/HOLDOUT_ANALYSIS.md — train vs holdout analysis.
* docs/reports/FINAL_REPORT.md — final result summary.
* docs/DOD.md — Definition of Done checklist.
* docs/REPORT_TEMPLATE.md — post-evolution run report template.
* docs/prompts/review_and_harden.md — review/hardening prompt for code review agents.

Style Conventions

Use:

* type hints everywhere;
* PEP 484 / modern Python union syntax where appropriate;
* snake_case for functions and variables;
* SCREAMING_SNAKE_CASE for module-level constants;
* English comments and documentation;
* simple, deterministic code over clever abstractions.

Tests should use:

* pytest;
* plain assertions;
* minimal fixtures;
* no unnecessary conftest.py.

Agent Instructions

When modifying this repository, agents must:

1. Preserve the OpenEvolve contract.
2. Run task lint or equivalent syntax checks.
3. Run task test.
4. Run train and holdout evaluation when changing policy/evaluator/scenario logic.
5. Update documentation when experiment results or artifact paths change.
6. Keep negative results visible.
7. Avoid claiming production readiness.
8. Avoid moving artifacts without updating links.
9. Keep the repository readable as a public portfolio case study.
10. Prefer small, reviewable changes over large rewrites.

Definition of Done

A change is complete only when:

task lint
task test
task eval:train
task eval:holdout

all pass or failures are explicitly documented with a reason.

For documentation-only changes:

* markdown links must resolve;
* paths to experiment artifacts must be correct;
* claims must match committed evidence;
* README must remain readable as the main entry point.

Positioning

This repository supports the following professional positioning:

Building evaluation-first AI systems for QA automation, reliability testing, and complex workflow validation.

Keep the project aligned with that message.

The repo should demonstrate practical experience with:

* LLM-assisted development;
* local model experimentation;
* evolutionary optimization;
* deterministic evaluation;
* QA/reliability engineering;
* holdout validation;
* failure analysis;
* documenting AI system limitations honestly.