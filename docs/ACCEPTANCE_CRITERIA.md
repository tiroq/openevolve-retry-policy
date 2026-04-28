# Acceptance Criteria

A candidate evolved by OpenEvolve is **not accepted** until it passes every
gate below. Gates are grouped into hard, behavioral, and holdout layers.
Acceptance is constraint-first: a high `combined_score` does not override
any gate.

## 1. Hard gates (must pass; binary)

These are non-negotiable. Failure on any gate = automatic rejection.

- [ ] Program imports successfully (no syntax / import errors)
- [ ] `choose_action` signature is preserved exactly:
  ```python
  choose_action(
      attempt: int,
      error_type: str,
      elapsed_ms: int,
      last_rtt_ms: int,
      consecutive_failures: int,
      is_idempotent: bool,
      circuit_open: bool,
  ) -> Dict[str, int | str]
  ```
- [ ] Return shape preserved: `{"action": str, "wait_ms": int}`
- [ ] `action` is one of `{"retry", "fail", "switch_endpoint", "open_circuit"}`
- [ ] `wait_ms` is a non-negative integer
- [ ] No undefined variables referenced
- [ ] No new imports of network / IO modules
- [ ] No external state, no file or network access
- [ ] No use of randomness unless explicitly justified and deterministic
- [ ] `runs_successfully == 1.0` on both train and holdout
- [ ] `dangerous_non_idempotent_retries == 0.0` on both train and holdout

## 2. Behavioral gates (must pass; observed in evaluator)

- [ ] Train `combined_score` >= baseline train `combined_score` *or*
      the regression is justified by an improvement on a more
      important behavioral metric (e.g. success rate).
- [ ] `useless_retries` not materially worse than baseline.
- [ ] `avg_latency_ms` improvement is not achieved primarily by failing
      fast on recoverable scenarios.
- [ ] When `circuit_open == True`, the policy fails immediately.
- [ ] When `error_type` is non-retryable, the policy fails fast.
- [ ] When `is_idempotent == False` and `attempt > 0`, the policy does
      not retry.

## 3. Holdout gates (must pass)

- [ ] Holdout `runs_successfully == 1.0`.
- [ ] Holdout `success_rate` is **not materially worse** than baseline
      (working threshold: no more than ~5 percentage points down,
      reviewed manually).
- [ ] Holdout `combined_score` is not catastrophically worse than baseline.
- [ ] No new failure mode appears only on holdout (e.g. an error type that
      now triggers an open circuit when it should retry).

## 4. Safety-first interpretation

When metrics conflict, the priority order is:

1. Safety (`dangerous_non_idempotent_retries`, runs successfully, no crash)
2. Reliability (`success_rate` on holdout)
3. Useful behavior (`good_fail_fast_decisions`, `good_endpoint_switches`)
4. Efficiency (`avg_latency_ms`, `avg_retry_count`, `useless_retries`)
5. Aggregate (`combined_score`)

A candidate that improves (4) and (5) but regresses (2) is **rejected**.

## 5. Rejection rules

A candidate is rejected if any of the following hold:

- Any hard gate fails.
- Holdout `success_rate` regresses by more than the working threshold.
- The diff is suspiciously large (rewrites outside the EVOLVE-BLOCK,
  changes to helper code, new imports).
- The diff contains placeholders, prose, TODOs, or unreachable branches.
- Latency improvement is explained mostly by faster failure rather than
  smarter recovery.

## 6. Candidate review checklist

Run this for every candidate considered for promotion:

- [ ] Program imports successfully
- [ ] `choose_action` signature preserved
- [ ] Return shape preserved
- [ ] No undefined variables
- [ ] No external state
- [ ] No dangerous non-idempotent retries
- [ ] Train metrics captured
- [ ] Holdout metrics captured
- [ ] Holdout `success_rate` not materially worse
- [ ] Combined score reviewed *with* the metric breakdown, not in isolation
- [ ] Diff reviewed by a human

## 7. Production note

This repository is a case study, not a production retry library. Even a
candidate that passes all gates above should be reviewed against the
target system's idempotency model, SLAs, and observability before being
adopted in any real client. The acceptance gates here are *necessary*
for trust, but not *sufficient* for production deployment.
