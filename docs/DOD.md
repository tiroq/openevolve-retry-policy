# Definition of Done

## Functional

- The repository can be cloned and understood without hidden context.
- `pytest -q` passes locally.
- `python evaluator.py --program initial_program.py --dataset train --json` succeeds.
- `python evaluator.py --program initial_program.py --dataset holdout --json` succeeds.
- `initial_program.py` contains exactly one evolve block for the core policy.
- `evaluator.py` returns a metric dictionary containing `combined_score`.

## Evolution-readiness

- The search space is intentionally narrow and local-model friendly.
- The evaluator penalizes dangerous non-idempotent retries.
- There is a train/holdout split.
- Scenario generation is deterministic for fixed seeds.
- Failure behavior is explicit and returns a clearly bad score instead of crashing silently.

## Quality

- README explains the purpose, workflow, risks, and evaluation metrics.
- A review/hardening prompt exists under `docs/prompts/`.
- The report template can be used after an evolution run.
- Code comments are in English.

## Stretch goals

- Add a second evaluator stage for adversarial scenarios.
- Add endpoint cost modeling.
- Add protocol-aware variants for FIX or gRPC.
- Export per-scenario traces as artifacts.
