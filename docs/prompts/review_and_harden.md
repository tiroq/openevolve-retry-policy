# Review and Harden OpenEvolve Repository

You are acting as a senior code reviewer and evaluator designer for an OpenEvolve repository.

Repository goal:

- evolve a retry/backoff policy for unstable HTTP-style integrations using OpenEvolve
- keep the evolve surface small
- support local models first
- enforce safety for non-idempotent operations

Your tasks:

1. Review the full repository structure and code.
2. Verify OpenEvolve compatibility assumptions.
3. Find correctness issues, fragile assumptions, reward-hacking opportunities, evaluator leakage, and missing tests.
4. Improve the code directly where justified.
5. Add or refine tests.
6. Produce a concise engineering report.

Mandatory checks:

- exactly one EVOLVE-BLOCK in the candidate program
- evaluator always returns combined_score
- deterministic train/holdout scenario generation for fixed seeds
- strong penalties for unsafe non-idempotent retries
- no silent evaluator crashes
- README and docs are consistent with actual code
- comments remain in English

Expected outputs:

- code patches
- new or updated tests
- a short report with sections:
  - What was broken?
  - What was fragile?
  - What was missing?
  - What changed?
  - Remaining risks
  - Next highest-leverage improvement

Definition of Done:

- all tests pass
- any new behavior is covered by tests
- report is written
- if OpenEvolve integration assumptions are uncertain, state them explicitly instead of inventing behavior
