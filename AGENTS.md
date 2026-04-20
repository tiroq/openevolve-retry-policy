# Project Guidelines

## Overview

OpenEvolve example that evolves a retry/backoff policy for unstable HTTP-style integrations. The evolved artifact is a single `choose_action()` function inside an `EVOLVE-BLOCK` in `initial_program.py`.

## Build and Test

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Evaluate baseline locally:

```bash
python evaluator.py --program initial_program.py --dataset train --json
python evaluator.py --program initial_program.py --dataset holdout --json
```

## Architecture

```
initial_program.py  →  choose_action() + normalize_action()
evaluator.py        →  loads program dynamically, runs scenarios, returns metrics
scenarios.py        →  deterministic train (seed=42) / holdout (seed=314) scenario sets
config.yaml         →  OpenEvolve run configuration (local models)
```

- `evaluator.py` exposes `evaluate(program_path) -> Dict[str, float]` for OpenEvolve and a CLI (`--program`, `--dataset`, `--json`).
- The primary optimization target is `combined_score`. All metrics are returned as floats.
- On any exception, the evaluator returns `combined_score = -1e9` and `runs_successfully = 0.0` — it never crashes silently.

## OpenEvolve Contract

- `initial_program.py` must contain **exactly one** `EVOLVE-BLOCK` delimited by `# EVOLVE-BLOCK-START` / `# EVOLVE-BLOCK-END`.
- Only code **inside** the block is mutated. Everything outside (constants, `normalize_action`, imports) is stable.
- `choose_action()` returns `{"action": str, "wait_ms": int}` where action ∈ {retry, fail, switch_endpoint, open_circuit}.
- `normalize_action()` clamps `wait_ms` to [0, 30000] and validates action type — acts as a safety net.

## Conventions

- **Type hints** everywhere (PEP 484 union syntax `int | None`).
- **snake_case** for functions/variables, **SCREAMING_SNAKE_CASE** for module-level constants.
- Comments in **English**.
- Tests use **pytest** with plain assertions — no fixtures, no conftest.

## Key Pitfalls

- Retrying a **non-idempotent** request after attempt 0 incurs a heavy penalty (`-25.0` per occurrence). Evolved policies must guard this.
- `recovery_attempt` and `recovery_after_elapsed_ms` are the two recovery modes in scenarios. If both are `None` and there's no endpoint switch path, the scenario is **unrecoverable** — fail-fast is the correct behavior.
- `primary_endpoint_bad_until_attempt == 99` is a sentinel meaning "primary never recovers; use endpoint switch."
- Scenario generation is **deterministic** for fixed seeds. Do not break seed-dependent reproducibility.

## Documentation

- [docs/DOD.md](docs/DOD.md) — Definition of Done checklist
- [docs/REPORT_TEMPLATE.md](docs/REPORT_TEMPLATE.md) — Post-evolution run report template
- [docs/prompts/review_and_harden.md](docs/prompts/review_and_harden.md) — Review/hardening prompt for code review agents
