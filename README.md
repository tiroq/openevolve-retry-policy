# openevolve-retry-policy

A minimal but production-minded OpenEvolve example that evolves a retry/backoff policy for unstable HTTP-style integrations.

The repository is designed for **local models** first:
- small, cheap `EVOLVE-BLOCK`
- fast deterministic evaluator
- synthetic scenarios with train/holdout split
- strong penalties for unsafe retry behavior
- pytest suite and a review prompt for hardening

## Why this example

Most OpenEvolve demos are academically clean but not immediately reusable in engineering workflows. This repo targets a practical class of problems:

- flaky upstream APIs
- unstable gateways
- transient overload and rate limits
- idempotent vs non-idempotent operations
- circuit-breaker style fail-fast behavior

The evolved artifact is not a whole client. It is a single policy function that decides whether to:

- retry
- fail
- switch endpoint
- open the circuit

That makes the search space small enough for local models while keeping the evaluator strict and meaningful.

## Repository layout

```text
.
├── AGENTS.md
├── docs/
│   ├── DOD.md
│   ├── REPORT_TEMPLATE.md
│   └── prompts/
│       └── review_and_harden.md
├── tests/
│   ├── test_evaluator.py
│   ├── test_policy_contract.py
│   └── test_scenarios.py
├── config.yaml
├── evaluator.py
├── initial_program.py
├── requirements.txt
└── scenarios.py
```

## OpenEvolve contract

This example follows the standard OpenEvolve pattern:
- `initial_program.py` contains a single editable `EVOLVE-BLOCK`
- `evaluator.py` returns metrics including `combined_score`
- `config.yaml` configures the run

The current OpenEvolve repository documents this pattern and uses `combined_score` as the primary optimization metric. It also supports OpenAI-compatible endpoints and example invocation via `openevolve-run.py ... initial_program.py evaluator.py --config config.yaml`.

## Quick start

### 1. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run tests

```bash
pytest -q
```

### 3. Run baseline evaluation locally

```bash
python evaluator.py --program initial_program.py --dataset train --json
python evaluator.py --program initial_program.py --dataset holdout --json
```

### 4. Run OpenEvolve

From inside this repository:

```bash
python /path/to/openevolve/openevolve-run.py initial_program.py evaluator.py --config config.yaml --iterations 50
```

## Using local models

OpenEvolve supports OpenAI-compatible APIs; practitioners in the project discussions have also tried local setups by pointing `api_base` to a local endpoint such as Ollama-compatible servers.

Typical local options:
- Ollama OpenAI-compatible endpoint
- vLLM OpenAI server
- LM Studio local server
- OptiLLM or equivalent wrappers

Example config snippet:

```yaml
llm:
  primary_model: "qwen2.5-coder:7b"
  secondary_model: "qwen2.5:7b-instruct"
  api_base: "http://127.0.0.1:11434/v1"
```

## Problem definition

The policy receives a small operational state:
- attempt number
- last error type
- total elapsed time
- last observed RTT
- consecutive failures
- whether the operation is idempotent
- whether the circuit is currently open

It must return an action payload:

```python
{
  "action": "retry" | "fail" | "switch_endpoint" | "open_circuit",
  "wait_ms": int
}
```

## Evaluation strategy

The evaluator simulates synthetic but structured failure patterns:
- timeout then recovery
- rate limit cooldown
- server busy until elapsed threshold
- permanent disconnect
- endpoint A bad, endpoint B healthy
- dangerous non-idempotent retry opportunities

Metrics include:
- `success_rate`
- `avg_latency_ms`
- `avg_retry_count`
- `dangerous_non_idempotent_retries`
- `useless_retries`
- `good_fail_fast_decisions`
- `good_endpoint_switches`
- `runs_successfully`
- `combined_score`

## Design principles

1. **Strict evaluator, tiny mutate surface**
   The LLM edits only one small function.

2. **Reward safety, not just persistence**
   Repeated retrying of non-idempotent actions is heavily penalized.

3. **Holdout split matters**
   The policy should improve on unseen scenarios, not merely overfit training seeds.

4. **Local-model friendly**
   The task is narrow enough that small-to-medium local code/instruct models can still make progress.

## Suggested workflow

1. Run the baseline on train and holdout.
2. Start OpenEvolve with 30 to 50 iterations.
3. Inspect best evolved policy.
4. Re-run evaluator on holdout.
5. Write a short report using `docs/REPORT_TEMPLATE.md`.
6. Use `docs/prompts/review_and_harden.md` to ask another agent to review and harden the repo.

## What might fail

- The synthetic world may be too toy-like.
- The combined score may be reward-hackable.
- Local models may generate invalid action shapes unless the evaluator enforces the contract.
- Train/holdout gap may reveal evaluator leakage.

## Weakest link

The weakest link is not the model. It is the realism and coverage of the simulator. If the scenario generator is weak, the evolved policy will optimize for a world that does not exist.
