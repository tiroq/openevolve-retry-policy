# Evolution Progress Report

**Log file:** `openevolve_20260422_103145.log`  
**Start:** 2026-04-22 10:31:45  **End:** 2026-04-22 12:03:07  
**Model:** `qwen2.5-coder:1.5b`  **Seed:** 42  
**Iterations:** 50  **New-best events:** 1  
**Score:** -8.6781 → 1.1094  (Δ = +9.7875)

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
| `openevolve_output/logs/openevolve_20260422_103145.log` | Full run log |
| `openevolve_output/best/best_program.py` | Final best policy |
| `openevolve_output/best/best_program_info.json` | Final best metadata |
| `openevolve_output/checkpoints/checkpoint_5/` | 6 programs, best=1.1094 |
| `openevolve_output/checkpoints/checkpoint_10/` | 11 programs, best=1.1094 |
| `openevolve_output/checkpoints/checkpoint_15/` | 16 programs, best=1.1094 |
| `openevolve_output/checkpoints/checkpoint_20/` | 21 programs, best=1.1094 |
| `openevolve_output/checkpoints/checkpoint_25/` | 26 programs, best=1.1094 |
| `openevolve_output/checkpoints/checkpoint_30/` | 31 programs, best=1.1094 |
| `openevolve_output/checkpoints/checkpoint_35/` | 36 programs, best=1.1094 |
| `openevolve_output/checkpoints/checkpoint_40/` | 41 programs, best=1.1094 |
| `openevolve_output/checkpoints/checkpoint_45/` | 46 programs, best=1.1094 |
| `openevolve_output/checkpoints/checkpoint_50/` | 51 programs, best=1.1094 |

## Iteration Timeline

| Iter | Program (short) | Parent (short) | combined_score | success_rate | avg_latency_ms | avg_retry_count | useless_retries | good_switches | fail_fast | dur_s | 🌟 |
|------|-----------------|----------------|---------------|-------------|----------------|----------------|----------------|--------------|-----------|-------|-----|
| 1 | `0c6b98ae` | `8468d2e3` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 105.9 | ✅ |
| 2 | `db8a075a` | `8468d2e3` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 61.8 |  |
| 3 | `1763dd43` | `0c6b98ae` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 160.8 |  |
| 4 | `d9c57f95` | `8468d2e3` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 163.3 |  |
| 5 | `afdc92ea` | `1763dd43` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 116.2 |  |
| 6 | `0e471fb9` | `8468d2e3` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 108.0 |  |
| 7 | `4ffaa236` | `8468d2e3` | -4.5062 | 0.3750 | 952.81 | 2.4688 | 0.8750 | 0.0000 | 0.1875 | 107.6 |  |
| 8 | `cef35faf` | `d9c57f95` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 107.2 |  |
| 9 | `89aea788` | `d9c57f95` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 110.9 |  |
| 10 | `9a0d5562` | `0e471fb9` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 108.3 |  |
| 11 | `348cecf6` | `89aea788` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 107.7 |  |
| 12 | `b9a5b25e` | `db8a075a` | -4.5062 | 0.3750 | 952.81 | 2.4688 | 0.8750 | 0.0000 | 0.1875 | 106.9 |  |
| 13 | `f9b70916` | `89aea788` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 107.8 |  |
| 14 | `135b32ad` | `1763dd43` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 108.5 |  |
| 15 | `01b21142` | `8468d2e3` | -4.5062 | 0.3750 | 952.81 | 2.4688 | 0.8750 | 0.0000 | 0.1875 | 107.5 |  |
| 16 | `eb5ab991` | `4ffaa236` | -4.5062 | 0.3750 | 952.81 | 2.4688 | 0.8750 | 0.0000 | 0.1875 | 107.8 |  |
| 17 | `96a04a3b` | `db8a075a` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 108.8 |  |
| 18 | `19ec6554` | `eb5ab991` | -4.5062 | 0.3750 | 952.81 | 2.4688 | 0.8750 | 0.0000 | 0.1875 | 105.4 |  |
| 19 | `45ec9b12` | `afdc92ea` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 107.9 |  |
| 20 | `4f94899e` | `19ec6554` | -4.5062 | 0.3750 | 952.81 | 2.4688 | 0.8750 | 0.0000 | 0.1875 | 105.8 |  |
| 21 | `e2dd3c81` | `eb5ab991` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 108.3 |  |
| 22 | `2e6abc3b` | `01b21142` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 107.6 |  |
| 23 | `2bdc3eba` | `96a04a3b` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 107.3 |  |
| 24 | `d972cd3e` | `96a04a3b` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 108.5 |  |
| 25 | `e0473ff0` | `0e471fb9` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 108.5 |  |
| 26 | `3090c60e` | `89aea788` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 108.6 |  |
| 27 | `debf5ec8` | `2e6abc3b` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 107.2 |  |
| 28 | `0b2a75c1` | `d9c57f95` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 107.8 |  |
| 29 | `322bb736` | `19ec6554` | -4.5062 | 0.3750 | 952.81 | 2.4688 | 0.8750 | 0.0000 | 0.1875 | 105.2 |  |
| 30 | `ac6e1092` | `348cecf6` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 107.5 |  |
| 31 | `c1eaf05d` | `45ec9b12` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 108.8 |  |
| 32 | `669784a8` | `135b32ad` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 106.9 |  |
| 33 | `64ef1981` | `322bb736` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 108.5 |  |
| 34 | `1c4c3d59` | `669784a8` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 105.3 |  |
| 35 | `d9e2c28b` | `cef35faf` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 109.1 |  |
| 36 | `83bca17d` | `afdc92ea` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 111.2 |  |
| 37 | `27a08f9b` | `96a04a3b` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 108.8 |  |
| 38 | `abbee3b4` | `135b32ad` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 108.8 |  |
| 39 | `2cdb1f3e` | `2bdc3eba` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 109.3 |  |
| 40 | `35d10a20` | `19ec6554` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 107.8 |  |
| 41 | `451ff825` | `4ffaa236` | -4.5062 | 0.3750 | 952.81 | 2.4688 | 0.8750 | 0.0000 | 0.1875 | 108.0 |  |
| 42 | `efd3d09f` | `96a04a3b` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 110.1 |  |
| 43 | `712551ec` | `eb5ab991` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 109.5 |  |
| 44 | `a6c5bc50` | `96a04a3b` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 109.2 |  |
| 45 | `f284835f` | `2bdc3eba` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 115.5 |  |
| 46 | `e7f62b6f` | `135b32ad` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 108.4 |  |
| 47 | `756cd718` | `1c4c3d59` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 105.1 |  |
| 48 | `6549535c` | `afdc92ea` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 109.3 |  |
| 49 | `a5e2584b` | `96a04a3b` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 109.8 |  |
| 50 | `806eb20f` | `d972cd3e` | 1.1094 | 0.3438 | 775.00 | 2.1562 | 0.6875 | 0.0000 | 0.2812 | 110.0 |  |

## Checkpoint Timeline

| Checkpoint | Programs | Best ID (short) | combined_score |
|-----------|----------|----------------|---------------|
| 5 | 6 | `0c6b98ae` | 1.1094 |
| 10 | 11 | `0c6b98ae` | 1.1094 |
| 15 | 16 | `0c6b98ae` | 1.1094 |
| 20 | 21 | `0c6b98ae` | 1.1094 |
| 25 | 26 | `0c6b98ae` | 1.1094 |
| 30 | 31 | `0c6b98ae` | 1.1094 |
| 35 | 36 | `0c6b98ae` | 1.1094 |
| 40 | 41 | `0c6b98ae` | 1.1094 |
| 45 | 46 | `0c6b98ae` | 1.1094 |
| 50 | 51 | `0c6b98ae` | 1.1094 |

## Best-Solution Transitions

### Transition 1 — iteration 1

**`8468d2e3` → `0c6b98ae`**  
combined_score: -8.6781 → 1.1094  (Δ = +9.7875)

#### Metrics Before / After

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4062 | 0.3438 | -0.0624 |
| `avg_latency_ms` | 1320.0000 | 775.0000 | -545.0000 |
| `avg_retry_count` | 2.0312 | 2.1562 | +0.1250 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.6875 | 0.0000 |
| `good_fail_fast_decisions` | 0.2812 | 0.2812 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0000 | 0.0000 |
| `combined_score` | -8.6781 | 1.1094 | +9.7875 |

#### Unified Diff (EVOLVE-BLOCK)

```diff
--- 8468d2e3 (before)
+++ 0c6b98ae (after)
@@ -29,12 +29,13 @@
     if attempt >= 3:
         return {"action": "fail", "wait_ms": 0}
 
+    # Simplified retry policy
     if error_type == "rate_limit":
-        wait_ms = min(500 * (2 ** attempt), 8_000)
+        wait_ms = min(100 * (2 ** attempt), 8_000)
     elif error_type == "server_busy":
-        wait_ms = min(250 * (2 ** attempt), 4_000)
+        wait_ms = min(50 * (2 ** attempt), 4_000)
     else:
-        wait_ms = min(100 * (2 ** attempt), 2_000)
+        wait_ms = min(10 * (2 ** attempt), 2_000)
 
     if last_rtt_ms > 2_000:
         wait_ms += 250
```

## Plateau Analysis

Longest plateau: **49 iterations** (iterations 2–50).

New-best events at iterations: 1.

> ⚠️ **21 iteration(s)** produced candidates with `dangerous_non_idempotent_retries > 0`.

## Final Summary

| Metric | Seed (`initial_program.py`) | Final best |
|--------|----------------------------|------------|
| `runs_successfully` | 1.0000 | 1.0000 |
| `success_rate` | 0.4062 | 0.3438 |
| `avg_latency_ms` | 1320.0000 | 775.0000 |
| `avg_retry_count` | 2.0312 | 2.1562 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.6875 |
| `good_fail_fast_decisions` | 0.2812 | 0.2812 |
| `good_endpoint_switches` | 0.0000 | 0.0000 |
| `combined_score` | -8.6781 | 1.1094 |

**Final best program ID:** `0c6b98ae-f0b9-4497-9391-6879b56162d4`

## Train vs Holdout Evaluation

Live evaluation of the **seed policy** (`initial_program.py`) and the **final best program** on the deterministic train and holdout scenario sets.

### Train Dataset

| Metric | Seed | Best | Δ (best − seed) |
|--------|------|------|-----------------|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4062 | 0.3438 | -0.0625 |
| `avg_latency_ms` | 1320.0000 | 775.0000 | -545.0000 |
| `avg_retry_count` | 2.0312 | 2.1562 | +0.1250 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.6875 | 0.0000 |
| `good_fail_fast_decisions` | 0.2812 | 0.2812 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0000 | 0.0000 |
| `combined_score` | -8.6781 | 1.1094 | +9.7875 |

### Holdout Dataset

| Metric | Seed | Best | Δ (best − seed) |
|--------|------|------|-----------------|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.5625 | 0.3750 | -0.1875 |
| `avg_latency_ms` | 2651.2500 | 2113.1250 | -538.1250 |
| `avg_retry_count` | 1.8125 | 2.0625 | +0.2500 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.4375 | 0.4375 | 0.0000 |
| `good_fail_fast_decisions` | 0.3125 | 0.3125 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0000 | 0.0000 |
| `combined_score` | -29.6938 | -32.9250 | -3.2312 |

---
*Report generated by `scripts/generate_report.py` from `openevolve_20260422_103145.log`.*