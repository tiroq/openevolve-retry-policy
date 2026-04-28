# Experiments

A pragmatic journal of observations from evolving the retry policy with
OpenEvolve across different model backends. This is not an exhaustive
benchmark and the candidate counts are small. Wording is intentionally
cautious; values that come from manual or proxy logs are marked as such.

## 1. Goal

Find out whether — and under what conditions — LLM-driven code evolution
can produce a *safer and faster* retry/backoff policy than the baseline,
without regressing reliability on unseen scenarios.

The unit being optimized is `choose_action()` in
[initial_program.py](initial_program.py). The unit doing the optimizing is
[evaluator.py](evaluator.py).

## 2. Evaluation philosophy

- The evaluator is the product. The policy is the artifact under test.
- Acceptance is **constraint-first**, not score-first.
- Train metrics drive the search loop; holdout metrics decide acceptance.
- Any candidate that violates safety (e.g. dangerous non-idempotent retries)
  is rejected regardless of its scalar score.
- Failure modes are catalogued, not silently retried.

## 3. Baseline metrics

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

The baseline already enforces safety (`dangerous_non_idempotent_retries == 0`)
and never crashes, but it leaves substantial headroom in `success_rate` and
`useless_retries`.

## 4. Model / endpoint rounds

| Round | Model | Endpoint | Result | Holdout verdict | Notes |
| --- | --- | --- | --- | --- | --- |
| Hosted | `google/gemma-4-26b-a4b-it` (illustrative cloud reference) | OpenRouter / OpenAI-compatible | Valid evolution observed | Useful baseline behavior | Cloud reference; faster turnaround than local models |
| Local large | `qwen3.6:35b-a3b` / `gemma4:e4b` (local) | Ollama-compatible | Slow runs; some no-diff / prose responses | Rejected / inconclusive | Local generation quality issues; long latency per candidate |
| Local small-coder | `qwen2.5-coder:1.5b` | Ollama / proxy | Train improvement observed | Holdout regression in candidate example | Good for fast iteration, requires gates |
| Tiny | `tinyllama:1.1b` | Ollama / proxy | Mostly invalid candidates | Rejected | Weak contract following |
| Tiny-coder | `qwen2.5-coder:0.5b` | Ollama / proxy | Many invalid / no-op candidates | Rejected | Too weak for reliable evolution |
| Small-coder | `qwen2.5-coder:3b` | Ollama / proxy | Minor train improvement | Needs holdout validation | Promising but slower / less stable than 1.5b |

These rows describe the *shape* of what was observed, not formally
reproducible results. Logs and best-program artifacts for several rounds
are committed under `round_*_openevolve_output/`.

## 5. Candidate examples

### 5.1 `qwen2.5-coder:1.5b`, train improvement

Observed in a manual run: train `combined_score` improved from `-8.6781`
to `+1.1094`, but `success_rate` dropped from `0.40625` to `0.34375`.

This is a textbook example of *scalar score improvement that still requires
holdout review*. The score went up, but the most operationally important
metric (success rate) went down.

### 5.2 `qwen2.5-coder:1.5b`, checkpoint_5 holdout

```json
{
  "avg_latency_ms": 2113.125,
  "avg_retry_count": 2.0625,
  "combined_score": -32.925,
  "dangerous_non_idempotent_retries": 0.0,
  "good_endpoint_switches": 0.0,
  "good_fail_fast_decisions": 0.3125,
  "runs_successfully": 1.0,
  "success_rate": 0.375,
  "useless_retries": 0.4375
}
```

Compared to baseline holdout (`success_rate=0.5625`), this candidate is a
**regression**. Latency improved but reliability dropped. Rejected.

### 5.3 Another run, checkpoint_5 holdout

```json
{
  "avg_latency_ms": 2317.5,
  "avg_retry_count": 2.0625,
  "combined_score": -39.05625,
  "dangerous_non_idempotent_retries": 0.0,
  "good_endpoint_switches": 0.0,
  "good_fail_fast_decisions": 0.3125,
  "runs_successfully": 1.0,
  "success_rate": 0.375,
  "useless_retries": 0.4375
}
```

Same shape: lower success rate, worse combined score on holdout. Rejected.

### 5.4 `qwen2.5-coder:3b`, short run, train

```json
{
  "runs_successfully": 1.0,
  "success_rate": 0.34375,
  "avg_latency_ms": 1044.375,
  "avg_retry_count": 2.125,
  "dangerous_non_idempotent_retries": 0.0,
  "useless_retries": 0.6875,
  "good_fail_fast_decisions": 0.28125,
  "good_endpoint_switches": 0.0,
  "combined_score": -6.8937
}
```

Train `combined_score` improved from `-8.6781` to `-6.8937`. Promising,
but `success_rate` dropped vs baseline. Not auto-accepted; would require
holdout validation and a manual diff review.

## 6. Holdout analysis

See [docs/reports/HOLDOUT_ANALYSIS.md](docs/reports/HOLDOUT_ANALYSIS.md).
Summary:

- Baseline holdout `success_rate` = `0.5625`.
- Candidate holdout `success_rate` in the examples above = `0.375`.
- Combined score moved in different directions on train vs holdout.
- A candidate that "looks better" by combined score on train can be
  materially worse in production-like conditions.

## 7. Accepted / rejected / inconclusive

- **Accepted (none, formally):** No candidate has yet cleared every hard
  gate *and* matched or improved baseline holdout `success_rate`.
- **Rejected:** the `qwen2.5-coder:1.5b` checkpoint_5 candidates above,
  due to holdout regression. All `tinyllama:1.1b` and
  `qwen2.5-coder:0.5b` outputs that violated the contract.
- **Inconclusive / promising:** the `qwen2.5-coder:3b` short-run train
  result; needs holdout evaluation and human diff review.

## 8. Failure modes

Detailed in [docs/MODEL_FAILURE_MODES.md](docs/MODEL_FAILURE_MODES.md).
Most common in this repo's runs:

- no meaningful diff
- prose instead of complete code
- changed function signature
- invalid return shape (e.g. `wait_time` instead of `wait_ms`)
- undefined variables (`last_request_latency`, `error_code`)
- excessive rewrite outside the intended mutation area
- repeated invalid candidates from very small models
- candidates that improve latency by failing fast (reward hacking)

## 9. Key finding

> A candidate can improve a scalar train score by reducing latency while
> lowering success rate. In QA / reliability work, this is not necessarily
> an improvement. Acceptance must be based on hard gates plus holdout
> behavior.

## 10. Conclusion

LLM-driven code evolution can produce valid, contract-respecting
mutations even from small local models, but **the evaluator and acceptance
gates do most of the work**. Without strict QA-style validation and a
holdout split, the search will gladly drift into reward hacking or
holdout-regressing optimizations.

This is the central message of the project: the evaluator is the product.
