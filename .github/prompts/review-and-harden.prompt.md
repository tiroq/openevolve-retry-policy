---
description: "Review and harden the OpenEvolve retry-policy repo. Use when: code review, finding bugs, checking evaluator correctness, hardening tests, verifying OpenEvolve contract."
agent: "agent"
---

You are acting as a senior code reviewer and evaluator designer for this OpenEvolve repository.

Review the full repository, guided by [AGENTS.md](../../AGENTS.md) for project context.

## Tasks

1. Review the full repository structure and code.
2. Verify OpenEvolve compatibility assumptions.
3. Find correctness issues, fragile assumptions, reward-hacking opportunities, evaluator leakage, and missing tests.
4. Improve the code directly where justified.
5. Add or refine tests.
6. Produce a concise engineering report.

## Mandatory Checks

- Exactly one `EVOLVE-BLOCK` in the candidate program
- Evaluator always returns `combined_score`
- Deterministic train/holdout scenario generation for fixed seeds
- Strong penalties for unsafe non-idempotent retries
- No silent evaluator crashes
- README and docs are consistent with actual code
- Comments remain in English

## Expected Outputs

- Code patches
- New or updated tests
- A short report following [docs/REPORT_TEMPLATE.md](../../docs/REPORT_TEMPLATE.md) with sections:
  - What was broken?
  - What was fragile?
  - What was missing?
  - What changed?
  - Remaining risks
  - Next highest-leverage improvement

## Definition of Done

See [docs/DOD.md](../../docs/DOD.md). Additionally:
- All tests pass (`pytest -q`)
- Any new behavior is covered by tests
- Report is written
- If OpenEvolve integration assumptions are uncertain, state them explicitly instead of inventing behavior
