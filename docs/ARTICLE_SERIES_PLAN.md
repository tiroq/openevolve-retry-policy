# Article Series Plan: Evaluation-First AI Engineering

A planned set of public write-ups (LinkedIn / Medium / personal blog)
based on this repository. The thesis across all articles is the same:

> LLMs can propose code changes, but evaluator design, safety gates,
> holdout validation, and QA discipline determine whether the generated
> behavior is actually useful. *The evaluator is the product.*

Each entry below is an outline, not a finished post.

---

## 1. I Tried to Evolve a Retry Policy with Local LLMs

- **Audience.** Backend engineers, SDETs, AI-curious developers.
- **Thesis.** A small local-LLM + OpenEvolve setup can propose valid
  retry-policy changes, but only because the evaluator does most of the
  work.
- **Repo artifacts.** [README.md](../README.md),
  [initial_program.py](../initial_program.py),
  [evaluator.py](../evaluator.py).
- **Charts/tables.** Baseline train vs holdout metrics; iteration loop
  diagram.
- **Conclusion.** A working setup is achievable on a laptop. Quality of
  the evaluator decides whether the result is meaningful.

## 2. The Evaluator Was the Real Product

- **Audience.** AI tooling builders, engineering managers.
- **Thesis.** In any AI-assisted code-change loop, the evaluator and
  acceptance gates contain more engineering value than any single
  candidate.
- **Repo artifacts.** [evaluator.py](../evaluator.py),
  [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md),
  [scenarios.py](../scenarios.py).
- **Charts/tables.** Metric breakdown table; safety counters.
- **Conclusion.** Spend your engineering budget on the evaluator first.

## 3. Train Score Lied: Why Holdout Validation Matters

- **Audience.** SDETs, reliability engineers, ML-curious backend devs.
- **Thesis.** Train-score improvements can hide holdout regressions.
  Holdout is mandatory.
- **Repo artifacts.**
  [docs/reports/HOLDOUT_ANALYSIS.md](reports/HOLDOUT_ANALYSIS.md),
  [EXPERIMENTS.md](../EXPERIMENTS.md).
- **Charts/tables.** Train vs holdout `success_rate` for baseline and
  candidates; combined-score-vs-success-rate scatter.
- **Conclusion.** Constraint-first acceptance, not score-first.

## 4. Local LLM Failure Modes in Code Evolution

- **Audience.** AI tooling builders, prompt engineers.
- **Thesis.** Small local models fail in distinctive ways (no-op,
  contract drift, invalid keys, prose). These can be defended against.
- **Repo artifacts.**
  [docs/MODEL_FAILURE_MODES.md](MODEL_FAILURE_MODES.md),
  [tests/](../tests/).
- **Charts/tables.** Failure-mode taxonomy table; before/after diff
  examples.
- **Conclusion.** Contract layer + behavioral layer = practical defense.

## 5. Building QA Gates for AI-Generated Behavior

- **Audience.** QA automation engineers, SDETs.
- **Thesis.** Acceptance for AI-generated code looks a lot like a good
  QA test plan: hard gates, behavioral checks, regression detection.
- **Repo artifacts.** [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md),
  [tests/test_policy_contract.py](../tests/test_policy_contract.py).
- **Charts/tables.** Gate hierarchy diagram; rejection-rule table.
- **Conclusion.** QA discipline is the bottleneck for trustworthy
  AI-assisted code change.

## 6. From Retry Policies to FinTech Protocol Testing

- **Audience.** Fintech / trading-system engineers, reliability engineers.
- **Thesis.** The retry-policy pattern (narrow surface, deterministic
  evaluator, train/holdout) maps directly to FIX message lifecycle
  validation, post-trade reconciliation, and order-routing edge cases.
- **Repo artifacts.** [docs/POSITIONING.md](POSITIONING.md),
  [LESSONS_LEARNED.md](../LESSONS_LEARNED.md).
- **Charts/tables.** Mapping table from retry-policy primitives to
  FIX-session primitives.
- **Conclusion.** This pattern is reusable for higher-stakes domains.

## 7. What I Would Build Next: Evaluation-First QA Tooling

- **Audience.** Engineering managers, AI tooling builders, recruiters.
- **Thesis.** A productized evaluation-first harness — generic enough to
  cover retry policies, FIX validators, document QA, and LLM-output
  regression — is a high-leverage build.
- **Repo artifacts.** README "Next steps",
  [docs/POSITIONING.md](POSITIONING.md).
- **Charts/tables.** Tooling architecture sketch; reuse map across
  domains.
- **Conclusion.** Evaluation-first AI tooling is a viable product
  direction, not just an engineering practice.
