# Evolution Progress Report

**Log file:** `openevolve_20260422_180722.log`  
**Start:** 2026-04-22 18:07:22  **End:** 2026-04-22 22:00:43  
**Model:** `qwen2.5-coder:3b`  **Seed:** 42  
**Iterations:** 50  **New-best events:** 1  
**Score:** -8.6781 → -6.8937  (Δ = +1.7844)

## Source Files

| File | Role |
|------|------|
| `initial_program.py` | Seed policy (EVOLVE-BLOCK is mutated) |
| `evaluator.py` | Fitness function — returns `combined_score` |
| `scenarios.py` | Deterministic train/holdout scenario generator |
| `config.yaml` | OpenEvolve run configuration |

## Output Inventory

| Path | Contents |
|------|----------|
| `openevolve_output/logs/openevolve_20260422_180722.log` | Full run log |
| `openevolve_output/best/best_program.py` | Final best policy |
| `openevolve_output/best/best_program_info.json` | Final best metadata |
| `openevolve_output/checkpoints/checkpoint_5/` | 6 programs, best=-6.8937 |
| `openevolve_output/checkpoints/checkpoint_10/` | 11 programs, best=-6.8937 |
| `openevolve_output/checkpoints/checkpoint_15/` | 16 programs, best=-6.8937 |
| `openevolve_output/checkpoints/checkpoint_20/` | 21 programs, best=-6.8937 |
| `openevolve_output/checkpoints/checkpoint_25/` | 26 programs, best=-6.8937 |
| `openevolve_output/checkpoints/checkpoint_30/` | 31 programs, best=-6.8937 |
| `openevolve_output/checkpoints/checkpoint_35/` | 36 programs, best=-6.8937 |
| `openevolve_output/checkpoints/checkpoint_40/` | 41 programs, best=-6.8937 |
| `openevolve_output/checkpoints/checkpoint_45/` | 46 programs, best=-6.8937 |
| `openevolve_output/checkpoints/checkpoint_50/` | 51 programs, best=-6.8937 |

## Iteration Timeline

| Iter | Program (short) | Parent (short) | combined_score | success_rate | avg_latency_ms | avg_retry_count | useless_retries | good_switches | fail_fast | dur_s | 🌟 |
|------|-----------------|----------------|---------------|-------------|----------------|----------------|----------------|--------------|-----------|-------|-----|
| 1 | `e7aff120` | `035f4415` | -8.6781 | 0.4062 | 1320.00 | 2.0312 | 0.6875 | 0.0000 | 0.2812 | 132.5 |  |
| 2 | `ae89f404` | `035f4415` | -8.6781 | 0.4062 | 1320.00 | 2.0312 | 0.6875 | 0.0000 | 0.2812 | 79.0 |  |
| 3 | `3b1c981e` | `035f4415` | -6.8937 | 0.3438 | 1044.38 | 2.1250 | 0.6875 | 0.0000 | 0.2812 | 193.6 | ✅ |
| 4 | `f9a12b27` | `ae89f404` | -86.7031 | 0.4688 | 4150.00 | 1.7812 | 0.6875 | 0.0000 | 0.2812 | 215.7 |  |
| 5 | `a7e1a2e4` | `ae89f404` | -50.5375 | 0.4375 | 2249.69 | 2.8438 | 1.0312 | 0.0000 | 0.0000 | 213.6 |  |
| 6 | `39c984db` | `e7aff120` | -17.5906 | 0.4688 | 1447.81 | 2.4375 | 0.8125 | 0.0000 | 0.1250 | 232.7 |  |
| 7 | `bed6d390` | `e7aff120` | -193.7188 | 0.5312 | 7489.06 | 2.2812 | 0.9688 | 0.0000 | 0.0312 | 212.5 |  |
| 8 | `40824369` | `39c984db` | -50.6063 | 0.4688 | 2550.94 | 2.4062 | 0.8125 | 0.0000 | 0.1250 | 238.3 |  |
| 9 | `7f6516d5` | `39c984db` | -219.8406 | 0.5312 | 8385.31 | 2.2500 | 1.0312 | 0.0000 | 0.0000 | 239.3 |  |
| 10 | `13fe67fc` | `a7e1a2e4` | -160.6438 | 0.5312 | 6352.19 | 2.3438 | 1.0312 | 0.0000 | 0.0000 | 213.8 |  |
| 11 | `ec2c96b3` | `f9a12b27` | -8.6875 | 0.4375 | 1421.88 | 2.0625 | 0.6875 | 0.0000 | 0.2812 | 221.2 |  |
| 12 | `c7f69a53` | `3b1c981e` | -193.7188 | 0.5312 | 7489.06 | 2.2812 | 0.9688 | 0.0000 | 0.0312 | 213.7 |  |
| 13 | `0d27b0fb` | `f9a12b27` | -209.8719 | 0.5000 | 8250.94 | 1.9375 | 0.8750 | 0.0000 | 0.1562 | 224.1 |  |
| 14 | `00081998` | `e7aff120` | -79.4234 | 0.5312 | 3790.16 | 2.1875 | 0.8125 | 0.0000 | 0.1250 | 233.9 |  |
| 15 | `404b9202` | `13fe67fc` | -160.6438 | 0.5312 | 6352.19 | 2.3438 | 1.0312 | 0.0000 | 0.0000 | 215.3 |  |
| 16 | `a03cceeb` | `ec2c96b3` | -62.4500 | 0.4688 | 3333.75 | 1.8750 | 0.6875 | 0.0000 | 0.2812 | 218.3 |  |
| 17 | `7428a928` | `3b1c981e` | -18.8250 | 0.4688 | 1491.56 | 2.4062 | 0.8125 | 0.0000 | 0.1250 | 226.5 |  |
| 18 | `053e38d1` | `a03cceeb` | -124.4750 | 0.4688 | 5305.94 | 1.9688 | 0.8750 | 0.0000 | 0.1875 | 216.3 |  |
| 19 | `25e1bff4` | `40824369` | -50.6063 | 0.4688 | 2550.94 | 2.4062 | 0.8125 | 0.0000 | 0.1250 | 1669.0 |  |
| 20 | `caa10520` | `0d27b0fb` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 239.0 |  |
| 21 | `eb95b336` | `7428a928` | -21.2016 | 0.4688 | 1570.78 | 2.4062 | 0.8125 | 0.0000 | 0.1250 | 233.5 |  |
| 22 | `a7dd59cf` | `e7aff120` | -50.6063 | 0.4688 | 2550.94 | 2.4062 | 0.8125 | 0.0000 | 0.1250 | 231.2 |  |
| 23 | `5f343e99` | `00081998` | -93.0387 | 0.5312 | 4244.00 | 2.1875 | 0.8125 | 0.0000 | 0.1250 | 235.9 |  |
| 24 | `6b55bef7` | `00081998` | -79.4234 | 0.5312 | 3790.16 | 2.1875 | 0.8125 | 0.0000 | 0.1250 | 229.3 |  |
| 25 | `35aff8bb` | `7f6516d5` | -194.2812 | 0.5312 | 7507.81 | 2.2812 | 0.9688 | 0.0000 | 0.0312 | 214.9 |  |
| 26 | `cb4f49de` | `7f6516d5` | -223.0281 | 0.5312 | 8491.56 | 2.2500 | 1.0312 | 0.0000 | 0.0000 | 239.0 |  |
| 27 | `188ed7d6` | `6b55bef7` | -86.5953 | 0.5312 | 4029.22 | 2.1875 | 0.8125 | 0.0000 | 0.1250 | 237.4 |  |
| 28 | `1230a7cf` | `035f4415` | -17.0312 | 0.4375 | 1700.00 | 2.0625 | 0.6875 | 0.0000 | 0.2812 | 223.6 |  |
| 29 | `994f87c8` | `0d27b0fb` | -251.0156 | 0.5312 | 9398.44 | 2.2500 | 1.0312 | 0.0000 | 0.0000 | 215.7 |  |
| 30 | `805914b8` | `c7f69a53` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 237.8 |  |
| 31 | `8098fd0b` | `40824369` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 237.6 |  |
| 32 | `8f083134` | `a7dd59cf` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 236.9 |  |
| 33 | `c3199c2a` | `8098fd0b` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 237.4 |  |
| 34 | `c7ba7866` | `25e1bff4` | -50.6063 | 0.4688 | 2550.94 | 2.4062 | 0.8125 | 0.0000 | 0.1250 | 235.1 |  |
| 35 | `ece05fa6` | `ec2c96b3` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 211.2 |  |
| 36 | `89d28090` | `035f4415` | -55.2938 | 0.4688 | 2707.19 | 2.4062 | 0.8125 | 0.0000 | 0.1250 | 235.0 |  |
| 37 | `7d52a0f6` | `caa10520` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 228.2 |  |
| 38 | `d9a9d1ce` | `c3199c2a` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 236.9 |  |
| 39 | `d9d1dab5` | `35aff8bb` | -194.2812 | 0.5312 | 7507.81 | 2.2812 | 0.9688 | 0.0000 | 0.0312 | 216.1 |  |
| 40 | `8b2d1622` | `ece05fa6` | -53.4813 | 0.4375 | 2347.81 | 2.8438 | 1.0312 | 0.0000 | 0.0000 | 237.2 |  |
| 41 | `00e2b58f` | `1230a7cf` | -34.6313 | 0.5000 | 2120.00 | 2.4375 | 0.8125 | 0.0000 | 0.1250 | 239.8 |  |
| 42 | `0cc438f0` | `00081998` | -89.3853 | 0.5312 | 4122.22 | 2.1875 | 0.8125 | 0.0000 | 0.1250 | 238.0 |  |
| 43 | `18e65c70` | `e7aff120` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 236.4 |  |
| 44 | `da64c705` | `d9d1dab5` | -194.2812 | 0.5312 | 7507.81 | 2.2812 | 0.9688 | 0.0000 | 0.0312 | 1632.4 |  |
| 45 | `b6319a1c` | `18e65c70` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 237.7 |  |
| 46 | `6bdf6448` | `404b9202` | -141.0500 | 0.5312 | 5699.06 | 2.3438 | 1.0312 | 0.0000 | 0.0000 | 210.2 |  |
| 47 | `bc28a0b8` | `0cc438f0` | -90.1166 | 0.5312 | 4146.59 | 2.1875 | 0.8125 | 0.0000 | 0.1250 | 236.5 |  |
| 48 | `007e2227` | `0cc438f0` | -37.7834 | 0.5000 | 2238.09 | 2.2812 | 0.8125 | 0.0000 | 0.1250 | 237.1 |  |
| 49 | `84acbc22` | `00081998` | -79.4234 | 0.5312 | 3790.16 | 2.1875 | 0.8125 | 0.0000 | 0.1250 | 234.8 |  |
| 50 | `73ecde89` | `00e2b58f` | -34.6313 | 0.5000 | 2120.00 | 2.4375 | 0.8125 | 0.0000 | 0.1250 | 238.0 |  |

## Checkpoint Timeline

| Checkpoint | Programs | Best ID (short) | combined_score |
|-----------|----------|----------------|---------------|
| 5 | 6 | `3b1c981e` | -6.8937 |
| 10 | 11 | `3b1c981e` | -6.8937 |
| 15 | 16 | `3b1c981e` | -6.8937 |
| 20 | 21 | `3b1c981e` | -6.8937 |
| 25 | 26 | `3b1c981e` | -6.8937 |
| 30 | 31 | `3b1c981e` | -6.8937 |
| 35 | 36 | `3b1c981e` | -6.8937 |
| 40 | 41 | `3b1c981e` | -6.8937 |
| 45 | 46 | `3b1c981e` | -6.8937 |
| 50 | 51 | `3b1c981e` | -6.8937 |

## Best-Solution Transitions

### Transition 1 — iteration 3

**`035f4415` → `3b1c981e`**  
combined_score: -8.6781 → -6.8937  (Δ = +1.7844)

#### Metrics Before / After

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4062 | 0.3438 | -0.0624 |
| `avg_latency_ms` | 1320.0000 | 1044.3750 | -275.6250 |
| `avg_retry_count` | 2.0312 | 2.1250 | +0.0938 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.6875 | 0.0000 |
| `good_fail_fast_decisions` | 0.2812 | 0.2812 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0000 | 0.0000 |
| `combined_score` | -8.6781 | -6.8937 | +1.7844 |

#### Unified Diff (EVOLVE-BLOCK)

```diff
--- 035f4415 (before)
+++ 3b1c981e (after)
@@ -15,7 +15,7 @@
     - wait_ms is a non-negative integer
     """
     if circuit_open:
-        return {"action": "fail", "wait_ms": 0}
+        return {"action": "open_circuit", "wait_ms": 5_000}
 
     if error_type not in RETRYABLE_ERRORS:
         return {"action": "fail", "wait_ms": 0}
@@ -29,13 +29,14 @@
     if attempt >= 3:
         return {"action": "fail", "wait_ms": 0}
 
+    # Adjusted logic for rate_limit and server_busy
+    wait_ms = min(100 * (2 ** attempt), 2_000)
     if error_type == "rate_limit":
-        wait_ms = min(500 * (2 ** attempt), 8_000)
+        wait_ms = min(wait_ms, 500 * (2 ** attempt))
     elif error_type == "server_busy":
-        wait_ms = min(250 * (2 ** attempt), 4_000)
-    else:
-        wait_ms = min(100 * (2 ** attempt), 2_000)
+        wait_ms = min(wait_ms, 250 * (2 ** attempt))
 
+    # Add a small delay for slow responses
     if last_rtt_ms > 2_000:
         wait_ms += 250
```

## Mutation Timing

| Stat | Value |
|------|-------|
| Iterations | 50 |
| Min | 79.0 s |
| Max | 1669.0 s |
| Avg | 280.0 s |
| Std dev | 281.1 s |
| Total wall time | 233m 19s |

**Slowest 3 iterations:**

| Iter | Program (short) | Duration (s) |
|------|-----------------|-------------|
| 19 | `25e1bff4` | 1669.0 |
| 44 | `da64c705` | 1632.4 |
| 41 | `00e2b58f` | 239.8 |

**Fastest 3 iterations:**

| Iter | Program (short) | Duration (s) |
|------|-----------------|-------------|
| 2 | `ae89f404` | 79.0 |
| 1 | `e7aff120` | 132.5 |
| 3 | `3b1c981e` | 193.6 |

## Plateau Analysis

Longest plateau: **47 iterations** (iterations 4–50).

New-best events at iterations: 3.

> ⚠️ **41 iteration(s)** produced candidates with `dangerous_non_idempotent_retries > 0`.

## Final Summary

| Metric | Seed (`initial_program.py`) | Final best |
|--------|----------------------------|------------|
| `runs_successfully` | 1.0000 | 1.0000 |
| `success_rate` | 0.4062 | 0.3438 |
| `avg_latency_ms` | 1320.0000 | 1044.3750 |
| `avg_retry_count` | 2.0312 | 2.1250 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.6875 |
| `good_fail_fast_decisions` | 0.2812 | 0.2812 |
| `good_endpoint_switches` | 0.0000 | 0.0000 |
| `combined_score` | -8.6781 | -6.8937 |

**Final best program ID:** `3b1c981e-7aed-4cc8-8f83-b15fc6209f51`

## Train vs Holdout Evaluation

Live evaluation of the **seed policy** (`initial_program.py`) and the **final best program** on the deterministic train and holdout scenario sets.

### Train Dataset

| Metric | Seed | Best | Δ (best − seed) |
|--------|------|------|-----------------|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4062 | 0.3438 | -0.0625 |
| `avg_latency_ms` | 1320.0000 | 1044.3750 | -275.6250 |
| `avg_retry_count` | 2.0312 | 2.1250 | +0.0938 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.6875 | 0.0000 |
| `good_fail_fast_decisions` | 0.2812 | 0.2812 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0000 | 0.0000 |
| `combined_score` | -8.6781 | -6.8937 | +1.7844 |

### Holdout Dataset

| Metric | Seed | Best | Δ (best − seed) |
|--------|------|------|-----------------|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.5625 | 0.3750 | -0.1875 |
| `avg_latency_ms` | 2651.2500 | 2317.5000 | -333.7500 |
| `avg_retry_count` | 1.8125 | 2.0625 | +0.2500 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.4375 | 0.4375 | 0.0000 |
| `good_fail_fast_decisions` | 0.3125 | 0.3125 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0000 | 0.0000 |
| `combined_score` | -29.6938 | -39.0562 | -9.3625 |

---
*Report generated by `scripts/generate_report.py` from `openevolve_20260422_180722.log`.*