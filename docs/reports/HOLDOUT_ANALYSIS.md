# Holdout Analysis

This note explains the core holdout lesson from the experiments in this
repository. It is intentionally short and focused.

## The setup

- Train scenarios — seed `42`, used by OpenEvolve for the search loop.
- Holdout scenarios — seed `314`, never seen by the search loop.
- Both sets are deterministic.

The point of the holdout is to detect cases where a candidate has
specialized to the train scenarios in ways that do not generalize.

## Baseline numbers

| Metric | Train | Holdout |
| --- | ---: | ---: |
| `success_rate` | 0.40625 | 0.5625 |
| `avg_latency_ms` | 1320.0 | 2651.25 |
| `combined_score` | -8.6781 | -29.6937 |
| `dangerous_non_idempotent_retries` | 0.0 | 0.0 |

Two things to notice:

1. The baseline's *holdout* `success_rate` (0.5625) is actually higher
   than its train `success_rate` (0.40625). The train set is harder.
2. Holdout `combined_score` is much worse than train, dominated by
   higher latency. Score and reliability are not aligned across sets.

## Candidate numbers

Two `checkpoint_5` candidates from `qwen2.5-coder:1.5b`-class runs:

| Metric | Baseline | Cand. A | Cand. B |
| --- | ---: | ---: | ---: |
| `success_rate` (holdout) | 0.5625 | 0.375 | 0.375 |
| `avg_latency_ms` (holdout) | 2651.25 | 2113.125 | 2317.5 |
| `combined_score` (holdout) | -29.6937 | -32.925 | -39.0562 |
| `dangerous_non_idempotent_retries` | 0.0 | 0.0 | 0.0 |

Both candidates **improved latency on holdout** but **regressed
reliability** by ~18 percentage points of `success_rate`. Combined score
also got worse.

## Why this matters

- Latency improved because the policy gave up earlier on more error
  types. That is the textbook reward-hacking shape.
- The harm is invisible to anyone looking only at "latency went down".
- A train-only acceptance loop, or a combined-score-only acceptance
  loop, would have shipped this regression.

## The rule

> Production-like acceptance should be **constraint-first**, not
> score-first.

Concretely, in this repo:

- Hard gates (safety, contract) must pass.
- Holdout `success_rate` must not regress materially.
- Combined score is one signal among many, not the deciding one.

See [ACCEPTANCE_CRITERIA.md](../../ACCEPTANCE_CRITERIA.md) for the full
gate list and rejection rules.
