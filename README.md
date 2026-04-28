# openevolve-retry-policy

An evaluation-first AI engineering case study for evolving a retry/backoff
policy with [OpenEvolve](https://github.com/codelion/openevolve), local LLMs,
strict QA-style gates, and holdout validation.

> **Positioning:** Building evaluation-first AI systems for QA automation,
> reliability testing, and complex workflow validation.
>
> **Core thesis:** *The evaluator is the product.* LLMs can propose code
> changes, but evaluator design, safety gates, holdout validation, and QA
> discipline determine whether the generated behavior is actually useful.

This repository is **not just a retry-policy toy example**. It is a small,
reproducible experiment in AI-assisted software behavior improvement:

- define a narrow mutation surface
- generate candidate policies with LLMs
- evaluate behavior deterministically
- reject unsafe or overfitted candidates
- compare train vs holdout performance
- document model failure modes and evaluator weaknesses

---

## 1. Overview

The system under test is a single function, `choose_action()`, that decides
how a client should react to a transient or permanent failure when calling an
unstable HTTP-style endpoint. Possible decisions are `retry`,
`switch_endpoint`, `open_circuit`, or `fail`.

OpenEvolve mutates only the code inside an `EVOLVE-BLOCK` in
[initial_program.py](initial_program.py). Everything else — the contract,
helper code, scenarios, and evaluator — is stable and is treated as the
*test harness* against which candidates are judged.

## 2. Why this matters

Retry/backoff is a deceptively small problem with big production consequences:

- flaky upstream APIs and gateways
- transient overload, rate limits, and slow responses
- non-idempotent operations where retrying is unsafe
- circuit-breaker style fail-fast behavior
- failover between endpoints

It is also a good *proxy task* for AI-assisted reliability work: the search
space is narrow enough for small local models, but the evaluator can encode
real QA-style invariants (safety, latency, success rate, generalization).

## 3. What this project demonstrates

- a **deterministic evaluator** with train/holdout splits
- a **narrow mutation surface** (one function inside one block)
- **hard safety gates** (e.g. dangerous non-idempotent retries are heavily
  penalized)
- **train vs holdout** comparison to detect reward hacking and overfitting
- **model failure-mode catalog** observed across local models
- a structured **acceptance checklist** for candidate review
- a **report template** for repeatable post-run analysis

## 4. Architecture

```
initial_program.py  ->  choose_action() inside an EVOLVE-BLOCK
evaluator.py        ->  loads program dynamically, runs scenarios, returns metrics
scenarios.py        ->  deterministic train (seed=42) / holdout (seed=314) sets
config.yaml         ->  OpenEvolve run configuration (local-friendly defaults)
tests/              ->  pytest contract checks
```

`evaluator.py` exposes `evaluate(program_path) -> Dict[str, float]` for
OpenEvolve and a CLI (`--program`, `--dataset`, `--json`). On any exception
the evaluator returns `combined_score = -1e9` and `runs_successfully = 0.0`
— it never crashes silently.

## 5. Repository map

```
.
├── README.md                         # This file
├── AGENTS.md                         # Project guidelines for coding agents
├── EXPERIMENTS.md                    # Experiment journal
├── ACCEPTANCE_CRITERIA.md            # Hard / behavioral / holdout gates
├── LESSONS_LEARNED.md                # Distilled insights
├── Taskfile.yml                      # Reproducible task runner entry points
├── config.yaml                       # OpenEvolve config (local LLMs)
├── evaluator.py                      # Deterministic evaluator + CLI
├── initial_program.py                # choose_action() with EVOLVE-BLOCK
├── scenarios.py                      # Train/holdout scenario generators
├── requirements.txt
├── docs/
│   ├── POSITIONING.md                # How this repo maps to QA / reliability work
│   ├── MODEL_FAILURE_MODES.md        # Observed LLM failure modes
│   ├── ARTICLE_SERIES_PLAN.md        # Outline of upcoming write-ups
│   ├── REPORT_TEMPLATE.md            # Per-run report template
│   ├── REPO_GUIDE.md                 # Where to look for what
│   ├── DOD.md                        # Definition of Done
│   ├── prompts/review_and_harden.md  # Review/hardening prompt
│   └── reports/
│       ├── FINAL_REPORT.md           # Polished case-study summary
│       ├── EXPERIMENT_LOG.md         # Chronological observations
│       └── HOLDOUT_ANALYSIS.md       # Train vs holdout deep dive
├── experiments/
│   ├── README.md
│   └── rounds/                       # Saved OpenEvolve artifacts (best / checkpoints / logs)
│       ├── round_1_cloud_openevolve_output/
│       ├── round_2_local_openevolve_output/
│       ├── round_3_local_openevolve_output/
│       ├── round_4_local_openevolve_output/
│       ├── round_5_local_openevolve_output/
│       └── round_7_local_openevolve_output/
├── tests/                            # pytest contract suite
└── scripts/                          # Helper scripts (report generation, post-edit hooks)
```

## 6. Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Or via [Task](https://taskfile.dev):

```bash
task install
```

## 7. Running tests

```bash
task test
```

Direct invocation:

```bash
pytest -q
```

## 8. Running baseline evaluation

```bash
task eval:train
task eval:holdout
# both at once
task eval
```

## 9. Running OpenEvolve

```bash
task evolve
# or with custom iteration count
ITERATIONS=20 task evolve
# or with debug logging
task evolve:debug
```

OpenEvolve must be installed (it is listed in `requirements.txt`). The run
configuration is in [config.yaml](config.yaml). Local model endpoints
(Ollama, vLLM, LM Studio, OptiLLM) are supported via OpenAI-compatible APIs.

## 10. Evaluating a candidate

The Taskfile supports overriding the evaluated program via the `CANDIDATE`
variable. The default is `initial_program.py`:

```bash
# default: evaluate baseline
task eval:holdout

# evaluate an evolved candidate (path is illustrative)
CANDIDATE=experiments/rounds/round_1_cloud_openevolve_output/best/best_program.py task eval:holdout

# evaluate a checkpoint
CANDIDATE=experiments/rounds/round_2_local_openevolve_output/checkpoints/checkpoint_5/best_program.py task eval:train
```

Save train + holdout JSON for a candidate in one shot:

```bash
CANDIDATE=path/to/candidate.py task report
# writes reports/train.json and reports/holdout.json
```

## 11. Baseline metrics

Train (seed=42):

```json
{
  "avg_latency_ms": 1320.0,
  "avg_retry_count": 2.03125,
  "combined_score": -8.678125,
  "dangerous_non_idempotent_retries": 0.0,
  "good_endpoint_switches": 0.0,
  "good_fail_fast_decisions": 0.28125,
  "runs_successfully": 1.0,
  "success_rate": 0.40625,
  "useless_retries": 0.6875
}
```

Holdout (seed=314):

```json
{
  "avg_latency_ms": 2651.25,
  "avg_retry_count": 1.8125,
  "combined_score": -29.69375,
  "dangerous_non_idempotent_retries": 0.0,
  "good_endpoint_switches": 0.0,
  "good_fail_fast_decisions": 0.3125,
  "runs_successfully": 1.0,
  "success_rate": 0.5625,
  "useless_retries": 0.4375
}
```

The train set is used for evolution / search. The holdout set is used only
for generalization checks and is not visible to the search loop.

## 12. Experiment summary

Multiple OpenEvolve rounds were performed against both hosted and local
models. See [EXPERIMENTS.md](EXPERIMENTS.md) for the full journal and
[docs/reports/FINAL_REPORT.md](docs/reports/FINAL_REPORT.md) for the polished
write-up.

A representative finding: a `qwen2.5-coder:1.5b` candidate improved train
`combined_score` from `-8.6781` to `+1.1094` while *reducing*
`success_rate` from `0.4062` to `0.3438`. On holdout, candidates from the
same family showed regressions (e.g. `success_rate` dropping from `0.5625`
to `0.375`). This is the canonical example of why scalar score must not be
the sole acceptance signal.

## 13. Key findings

- valid LLM-generated mutations are possible, including from small local models
- train score can be misleading; latency-driven score gains can mask reliability regressions
- holdout validation is mandatory, not optional
- local models exhibit distinct failure modes (no-diff, prose, contract drift, invalid keys)
- small local models can still be useful when the mutation surface is narrow
- scalar combined score is necessary but not sufficient for acceptance
- the evaluator is the main engineering artifact, not the policy itself
- the weakest link is evaluator/simulator realism

## 14. Acceptance criteria

A candidate must pass all of the following before being considered
accepted. Full checklist in
[ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md).

- program imports successfully
- `choose_action` signature preserved
- return shape preserved (`{"action": str, "wait_ms": int}`)
- `runs_successfully == 1.0`
- `dangerous_non_idempotent_retries == 0.0`
- no undefined variables, no external state, no network calls
- holdout `success_rate` not materially worse than baseline
- diff reviewed by a human

## 15. Model failure modes

Documented in [docs/MODEL_FAILURE_MODES.md](docs/MODEL_FAILURE_MODES.md).
Highlights:

- contract drift (changed signature)
- invalid payload keys (`wait_time` instead of `wait_ms`)
- undefined variables (`last_request_latency`, `error_code`)
- prose instead of code
- no-op mutations
- excessive rewrite outside the intended block
- reward hacking (improving latency by failing fast)
- repeated invalid candidates from very small models

## 16. What this project is *not*

- not a production retry library
- not a benchmark proving one model is best
- not a claim that LLMs can autonomously ship reliability logic
- not a replacement for domain-specific design review
- not a complete distributed-systems simulator

## 17. Known limitations

- the synthetic scenario set is small and stylized
- the evaluator does not model partial failures, jitter, or queue effects
- there is no adversarial scenario generator yet
- combined score weights are hand-tuned and reward-hackable
- holdout uses a single seed (`314`); deeper holdouts are future work

## 18. Next steps

- richer scenario generation (queueing effects, partial failures, jitter)
- better endpoint-switch / failover modeling
- multi-seed and adversarial holdouts
- mutation-testing-style stress scenarios
- automated per-run report generation
- model comparison matrix across local + hosted backends
- extension to fintech protocol / FIX message lifecycle validation
- extension to document-processing QA using mdify-style pipelines
- LLM output regression testing harness

## 19. Case study documents

- [EXPERIMENTS.md](EXPERIMENTS.md) — experiment journal
- [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md) — hard, behavioral, and holdout gates
- [LESSONS_LEARNED.md](LESSONS_LEARNED.md) — distilled lessons
- [docs/POSITIONING.md](docs/POSITIONING.md) — how this maps to QA / reliability work
- [docs/MODEL_FAILURE_MODES.md](docs/MODEL_FAILURE_MODES.md) — observed LLM failure modes
- [docs/REPORT_TEMPLATE.md](docs/REPORT_TEMPLATE.md) — per-run report template
- [docs/REPO_GUIDE.md](docs/REPO_GUIDE.md) — navigation guide
- [docs/reports/FINAL_REPORT.md](docs/reports/FINAL_REPORT.md) — polished case-study summary
- [docs/reports/EXPERIMENT_LOG.md](docs/reports/EXPERIMENT_LOG.md) — chronological log
- [docs/reports/HOLDOUT_ANALYSIS.md](docs/reports/HOLDOUT_ANALYSIS.md) — holdout deep dive

## 20. Article series

A planned set of public write-ups based on this repository is outlined in
[docs/ARTICLE_SERIES_PLAN.md](docs/ARTICLE_SERIES_PLAN.md). Topics include
evaluation-first AI engineering, train-vs-holdout traps, and applying these
patterns to fintech protocol testing and AI-assisted QA tooling.

## 21. License

See [LICENSE](LICENSE) if present, otherwise treat as personal case-study
material. External code (OpenEvolve, model weights) retains its own license.
