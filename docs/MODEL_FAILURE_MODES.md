# Model Failure Modes

A catalog of failure modes observed when using LLMs (mostly local) to
mutate the `choose_action()` function. Each entry includes a short
description, an example where useful, the operational impact, how it is
detected, and how it can be mitigated.

These observations come from manual and proxy log review across multiple
OpenEvolve runs. They are not exhaustive and are not formally measured
across a fixed sample.

---

## 1. Contract drift

**Description.** The model changes the function signature — adds, removes,
or renames parameters, or changes the return type.

**Example.**

```python
# Expected
def choose_action(attempt, error_type, elapsed_ms, last_rtt_ms,
                  consecutive_failures, is_idempotent, circuit_open): ...

# Drift
def choose_action(state, error): ...
```

**Impact.** The evaluator cannot call the function. The whole run fails
or returns the safety floor (`combined_score = -1e9`).

**Detection.** Pytest contract tests (`tests/test_policy_contract.py`),
plus the evaluator's import-time check.

**Mitigation.** Keep the EVOLVE-BLOCK small; constrain the prompt to
"return only the body"; add a signature-shape test.

---

## 2. Invalid payload keys

**Description.** The function returns a dict with the wrong keys.

**Example.**

```python
# Expected
{"action": "retry", "wait_ms": 100}

# Invalid
{"action": "retry", "wait_time": 100}
```

**Impact.** `wait_ms` becomes 0 after normalization (or `action` becomes
`"fail"`), silently degrading behavior.

**Detection.** Unit tests + evaluator's `normalize_action()` + explicit
contract checks.

**Mitigation.** Prompt constraints, stronger tests, smaller mutation
block, post-generation validation.

---

## 3. Undefined variables

**Description.** The model references variables that do not exist in the
function scope.

**Example.** `last_request_latency`, `error_code`, `now_ms`,
`global_state.endpoint`.

**Impact.** `NameError` at evaluation time. The evaluator returns the
safety floor.

**Detection.** Import / first-call execution; pytest; evaluator's broad
`except` returning `runs_successfully = 0.0`.

**Mitigation.** Prompt should enumerate available variables. Linting
candidates with `py_compile` plus a smoke call before scoring helps.

---

## 4. Prose instead of code

**Description.** The model returns natural-language text, sometimes wrapped
in fences, sometimes mixed with partial code.

**Impact.** Diff cannot be applied, or applied diff produces a syntax
error.

**Detection.** OpenEvolve diff parser failures; `py_compile` failure on
the resulting file.

**Mitigation.** Stricter system prompt, lower temperature, retry with a
"code only" instruction, smaller models with `coder` tuning.

---

## 5. No-op mutation

**Description.** The model returns the same code with cosmetic changes
(whitespace, renaming a local variable). The diff exists but the behavior
is identical.

**Impact.** Wasted iteration; evaluator runs but the score does not move.

**Detection.** Compare normalized AST or compare run metrics; identical
metrics across iterations are a signal.

**Mitigation.** Prompt nudges, temperature tuning, escape from this state
by injecting a different parent program. Tinier models (`tinyllama:1.1b`,
`qwen2.5-coder:0.5b`) hit this state often.

---

## 6. Over-aggressive simplification

**Description.** The model removes safety branches (e.g. the
non-idempotent guard) on the assumption they are dead code.

**Impact.** Hard safety gate trips: `dangerous_non_idempotent_retries > 0`.
Candidate is rejected.

**Detection.** Evaluator's safety counter; pytest contract tests.

**Mitigation.** Encode the safety branch as a penalty in the evaluator
(it already is) and as a unit test (it already is). Both layers must agree.

---

## 7. Reward hacking

**Description.** The model finds that failing fast on more error types
reduces latency and avoids useless retries, improving `combined_score`
even though `success_rate` drops.

**Impact.** The candidate looks better on aggregate but is operationally
worse.

**Detection.** Always inspect `success_rate` alongside `combined_score`.
Holdout regression is the canonical signal.

**Mitigation.** Re-weight the score; add explicit success-rate floor as
a hard gate; review diffs that primarily delete `retry` branches.

---

## 8. Excessive rewrite

**Description.** The model rewrites code outside the EVOLVE-BLOCK, or
changes helper functions / constants.

**Impact.** Either the diff is rejected by OpenEvolve, or the rewritten
helpers break unrelated tests.

**Detection.** Diff inspection; pytest run; the evaluator's stable-helper
contract.

**Mitigation.** Make the EVOLVE-BLOCK boundaries explicit in the prompt;
keep helpers minimal so there is little to rewrite.

---

## 9. Slow local inference

**Description.** Larger local models (e.g. `qwen3.6:35b-a3b` class) take
many seconds per candidate, slowing the loop to the point where the
evaluator is the cheapest part of the run.

**Impact.** Few iterations per wall-clock unit; harder to explore.

**Detection.** OpenEvolve logs / wall-clock per iteration.

**Mitigation.** Use smaller `coder` models for the bulk of iterations and
escalate to a larger model occasionally. Offload to a hosted model for
final polish.

---

## 10. Repeated invalid candidates

**Description.** Very small models (`tinyllama:1.1b`,
`qwen2.5-coder:0.5b`) produce the same invalid output across iterations.

**Impact.** The search loop stalls. No useful candidates are produced.

**Detection.** Repeated import / contract failures with similar
signatures across iterations.

**Mitigation.** Switch model. The evaluation harness is doing its job by
rejecting these; the model is simply too weak for the task surface.

---

## Summary

Most failure modes split cleanly into two layers of defense:

- **Contract layer** — tests, normalization, py_compile, signature checks.
  Catches contract drift, invalid keys, undefined variables, prose, and
  excessive rewrite.
- **Behavioral layer** — evaluator metrics, holdout split, safety
  counters. Catches no-op mutations, over-aggressive simplification, and
  reward hacking.

Both layers are necessary. Skipping either one lets entire categories of
bad candidates through.
