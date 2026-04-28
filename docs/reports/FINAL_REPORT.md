# Final Report — openevolve-retry-policy

A polished, honest summary of the current state of the experiment. This
report is intentionally cautious. It does not claim production readiness.
It documents the *shape* of a disciplined workflow for using LLMs to
propose behavior changes under strict QA evaluation.

> This experiment does not prove autonomous production readiness. It
> demonstrates the shape of a disciplined workflow for using LLMs to
> propose behavior changes under strict QA evaluation.

## 1. Executive summary

- **Subject under test.** A single function, `choose_action()`, deciding
  retry / fail / switch_endpoint / open_circuit for an unstable HTTP
  client.
- **Method.** OpenEvolve mutates one EVOLVE-BLOCK; a deterministic
  evaluator scores candidates on train and holdout scenario sets.
- **Outcome.** Multiple LLM backends produced valid, contract-respecting
  mutations. None of the candidates evaluated so far cleared every
  acceptance gate while improving holdout `success_rate`.
- **Headline finding.** A candidate can improve a scalar train score by
  reducing latency while lowering success rate. Acceptance must be based
  on hard gates plus holdout behavior, not on combined score alone.

## 2. System under test

- `choose_action(attempt, error_type, elapsed_ms, last_rtt_ms,
  consecutive_failures, is_idempotent, circuit_open) -> {"action", "wait_ms"}`
- One EVOLVE-BLOCK in [initial_program.py](../../initial_program.py).
- Deterministic train (seed=42) and holdout (seed=314) scenarios in
  [scenarios.py](../../scenarios.py).
- Evaluator in [evaluator.py](../../evaluator.py) — never crashes
  silently; on any exception returns `combined_score = -1e9`,
  `runs_successfully = 0.0`.

## 3. Baseline

Train:

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

Holdout:

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

## 4. Evaluation design

Three layers, all in the evaluator:

1. **Hard gates.** Import, signature, return shape, safety counters.
2. **Behavioral metrics.** `success_rate`, latency, retry counts,
   useless retries, fail-fast decisions, endpoint switches.
3. **Aggregate.** `combined_score`, used for search but not for final
   acceptance.

Train drives the search; holdout is held back for generalization checks.
Acceptance is **constraint-first** — see
[ACCEPTANCE_CRITERIA.md](../../ACCEPTANCE_CRITERIA.md).

## 5. Experiment rounds

See [EXPERIMENTS.md](../../EXPERIMENTS.md) for the full table. Summary:

- Hosted reference model — produced valid evolution; useful as a
  reliability baseline for the loop itself.
- Local large models — slow per iteration; some no-diff / prose
  responses; inconclusive.
- `qwen2.5-coder:1.5b` — fast iteration; produced contract-respecting
  diffs; some candidates regressed holdout.
- `qwen2.5-coder:3b` — minor train improvement; needs holdout
  validation.
- `tinyllama:1.1b`, `qwen2.5-coder:0.5b` — too weak for reliable
  evolution on this task.

## 6. Candidate examples

### 6.1 Train-improvement example

A `qwen2.5-coder:1.5b` run improved train `combined_score` from
`-8.6781` to `+1.1094` while reducing `success_rate` from `0.40625` to
`0.34375`. Useful illustration of scalar-score improvement that still
requires holdout review.

### 6.2 Holdout-regression examples

`qwen2.5-coder:1.5b` checkpoint_5:

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

Another run, checkpoint_5:

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

Both regressed holdout `success_rate` from `0.5625` to `0.375`.
Rejected.

### 6.3 Promising train result

`qwen2.5-coder:3b` short run, train `combined_score` improved from
`-8.6781` to `-6.8937`, with `success_rate=0.34375`. Not auto-accepted;
needs holdout evaluation and human diff review.

## 7. Holdout findings

See [HOLDOUT_ANALYSIS.md](HOLDOUT_ANALYSIS.md). Pattern:

- Train and holdout do not move together.
- Several candidates improved latency on holdout but lost reliability.
- Combined score alone would have accepted at least one candidate that
  the constraint-first acceptance correctly rejected.

## 8. Model failure modes

Detailed in [MODEL_FAILURE_MODES.md](../MODEL_FAILURE_MODES.md). Most
common in practice:

- contract drift
- invalid payload keys
- undefined variables
- prose instead of code
- no-op mutations
- excessive rewrite outside the EVOLVE-BLOCK
- reward hacking via fast failure

The contract layer (tests + normalization + py_compile) and the
behavioral layer (evaluator metrics + holdout) catch different
categories. Both are required.

## 9. Safety review

- `dangerous_non_idempotent_retries == 0.0` on baseline train and
  holdout, and on all evaluated candidates discussed in this report.
- No external state, no file or network access in the evaluator or the
  policy.
- Evaluator never crashes silently — exceptions return the safety floor.
- Pytest contract suite covers signature, return shape, and key
  invariants.

## 10. Conclusion

LLM-driven code evolution can produce valid, contract-respecting
mutations on this task even from small local models. None of the
candidates evaluated so far cleared every acceptance gate while
improving holdout reliability. The most useful output of this experiment
is not a better policy — it is a clear demonstration that:

- the evaluator is the product
- holdout validation is mandatory
- combined score alone is unsafe as an acceptance signal
- the failure-mode catalog is reusable across future runs and across
  domains beyond retry policy

## 11. What would be improved next

- Richer scenario generation (jitter, queueing, partial failures).
- Better endpoint-switch / failover modeling.
- Multi-seed and adversarial holdouts.
- Mutation-testing-style stress scenarios.
- Automated per-run report generation hooked into `task report`.
- Model comparison matrix across local + hosted backends.
- Re-weighted `combined_score` that explicitly penalizes success-rate
  loss.
- Extension of the same harness to FIX message lifecycle validation and
  document-processing QA.
