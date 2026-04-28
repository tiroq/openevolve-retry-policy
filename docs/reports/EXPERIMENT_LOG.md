# Experiment Log

A chronological log of observed runs and manual checks. Entries marked
*"observed in manual run"* come from operator notes and proxy logs; the
exact iteration files may not be committed. Entries that point to
committed artifacts under `experiments/rounds/round_*_openevolve_output/` are reproducible
to the extent that the original model + endpoint configuration is
available.

Order: oldest first.

---

## E1 — Baseline train

- Source: [initial_program.py](../../initial_program.py)
- Command: `task eval:train`
- Metrics:

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

- Notes: stable; safe; substantial headroom.

---

## E2 — Baseline holdout

- Command: `task eval:holdout`
- Metrics:

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

- Notes: holdout combined score is much worse than train, mostly
  because the holdout scenarios are slower. `success_rate` is actually
  higher than train, which is a useful baseline to preserve.

---

## E3 — `qwen2.5-coder:1.5b`, train improvement (observed in manual run)

- Train `combined_score`: `-8.6781` → `+1.1094`
- Train `success_rate`: `0.40625` → `0.34375`
- Verdict: not accepted; canonical reward-hacking pattern (latency
  improved, reliability dropped).

---

## E4 — `qwen2.5-coder:1.5b`, holdout regression (checkpoint_5)

- Source: a `checkpoint_5/best_program.py` from a `qwen2.5-coder:1.5b`
  run (artifact path varies by round directory).
- Holdout metrics:

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

- Verdict: rejected. Holdout `success_rate` regressed from `0.5625` to
  `0.375`.

---

## E5 — Another run, holdout regression (checkpoint_5)

- Holdout metrics:

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

- Verdict: rejected. Same regression shape as E4.

---

## E6 — `qwen2.5-coder:3b`, minor train improvement (observed)

- Train metrics:

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

- Verdict: inconclusive / promising. Holdout evaluation and human diff
  review pending.

---

## E7 — `tinyllama:1.1b` invalid-candidate run (observed)

- Mostly invalid candidates: contract drift, invalid keys, no-op diffs.
- Verdict: rejected; model too weak for this mutation surface.

---

## E8 — Local large model, no-diff / prose issues (observed)

- Models in the `qwen3.6:35b-a3b` / `gemma4:e4b` class.
- Slow per-iteration generation; intermittent prose-instead-of-code
  responses; some no-diff outputs.
- Verdict: inconclusive. Not a fault of the harness; reflects local
  generation quality and latency under this hardware.
