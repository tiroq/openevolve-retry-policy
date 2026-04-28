# Repo Guide

A short navigation guide for readers who land here from a CV, LinkedIn
profile, or article and want to find the substance quickly.

## If you have 2 minutes

- Read the top of [README.md](../README.md) — positioning, thesis, and
  baseline metrics.
- Skim [docs/POSITIONING.md](POSITIONING.md) — how this maps to QA,
  reliability, and complex workflow validation.

## If you have 10 minutes

- [README.md](../README.md) — full overview.
- [EXPERIMENTS.md](../EXPERIMENTS.md) — what was tried and what
  happened.
- [docs/reports/HOLDOUT_ANALYSIS.md](reports/HOLDOUT_ANALYSIS.md) — the
  central technical lesson, in one page.

## If you have 30 minutes

- [docs/reports/FINAL_REPORT.md](reports/FINAL_REPORT.md) — polished
  case-study summary.
- [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md) — hard, behavioral,
  and holdout gates.
- [docs/MODEL_FAILURE_MODES.md](MODEL_FAILURE_MODES.md) — observed LLM
  failure modes and defenses.
- [LESSONS_LEARNED.md](../LESSONS_LEARNED.md) — distilled insights.

## If you want to read the code

- [initial_program.py](../initial_program.py) — the function under
  evolution. EVOLVE-BLOCK is clearly marked.
- [evaluator.py](../evaluator.py) — deterministic evaluator. Hard
  gates, behavioral metrics, combined score.
- [scenarios.py](../scenarios.py) — train (seed=42) and holdout
  (seed=314) scenario generation.
- [tests/](../tests/) — contract and scenario tests.

## If you want to run something

- `task install` — set up venv and install dependencies.
- `task test` — run the pytest suite.
- `task eval` — evaluate baseline on train and holdout.
- `task evolve` — run OpenEvolve (requires a configured LLM endpoint).
- `CANDIDATE=path/to/program.py task eval:holdout` — evaluate a
  candidate.

## If you want to write about this

- [docs/ARTICLE_SERIES_PLAN.md](ARTICLE_SERIES_PLAN.md) — outlines for
  upcoming write-ups.
- [docs/REPORT_TEMPLATE.md](REPORT_TEMPLATE.md) — per-run report
  template.
