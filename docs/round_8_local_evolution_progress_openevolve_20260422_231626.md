# Evolution Progress Report

**Log file:** `openevolve_20260422_231626.log`  
**Start:** 2026-04-22 23:16:26  **End:** 2026-04-23 00:16:12  
**Model:** `qwen3-coder-next:cloud`  **Seed:** 42  
**Iterations:** 50  **New-best events:** 2  
**Score:** -8.6781 → 10.0906  (Δ = +18.7687)

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
| `openevolve_output/logs/openevolve_20260422_231626.log` | Full run log |
| `openevolve_output/best/best_program.py` | Final best policy |
| `openevolve_output/best/best_program_info.json` | Final best metadata |
| `openevolve_output/checkpoints/checkpoint_5/` | 6 programs, best=-8.6781 |
| `openevolve_output/checkpoints/checkpoint_10/` | 11 programs, best=-8.6781 |
| `openevolve_output/checkpoints/checkpoint_15/` | 16 programs, best=-8.6781 |
| `openevolve_output/checkpoints/checkpoint_20/` | 21 programs, best=-8.6781 |
| `openevolve_output/checkpoints/checkpoint_25/` | 26 programs, best=-4.3125 |
| `openevolve_output/checkpoints/checkpoint_30/` | 31 programs, best=-4.3125 |
| `openevolve_output/checkpoints/checkpoint_35/` | 36 programs, best=-4.3125 |
| `openevolve_output/checkpoints/checkpoint_40/` | 41 programs, best=-4.3125 |
| `openevolve_output/checkpoints/checkpoint_45/` | 46 programs, best=10.0906 |
| `openevolve_output/checkpoints/checkpoint_50/` | 51 programs, best=10.0906 |

## Iteration Timeline

| Iter | Program (short) | Parent (short) | combined_score | success_rate | avg_latency_ms | avg_retry_count | useless_retries | good_switches | fail_fast | dur_s | 🌟 |
|------|-----------------|----------------|---------------|-------------|----------------|----------------|----------------|--------------|-----------|-------|-----|
| 1 | `ae2514f0` | `fcb6b657` | -12.6156 | 0.4062 | 1451.25 | 2.0312 | 0.6875 | 0.0000 | 0.2812 | 165.4 |  |
| 2 | `e67de06b` | `fcb6b657` | -42.4375 | 0.4062 | 2390.62 | 2.0625 | 0.8438 | 0.0000 | 0.2812 | 77.5 |  |
| 3 | `653fb221` | `fcb6b657` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 116.5 |  |
| 4 | `3dc57dbb` | `e67de06b` | -8.6781 | 0.4062 | 1320.00 | 2.0312 | 0.6875 | 0.0000 | 0.2812 | 143.7 |  |
| 5 | `310e039e` | `e67de06b` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 110.0 |  |
| 6 | `0aacc564` | `3dc57dbb` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 44.8 |  |
| 7 | `f97b7d6a` | `3dc57dbb` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 79.3 |  |
| 8 | `da1043c6` | `0aacc564` | -18.3375 | 0.4062 | 1536.25 | 2.2500 | 0.8750 | 0.0000 | 0.1875 | 28.6 |  |
| 9 | `b1ff245e` | `0aacc564` | -8.6781 | 0.4062 | 1320.00 | 2.0312 | 0.6875 | 0.0000 | 0.2812 | 68.2 |  |
| 10 | `7ed3cc92` | `653fb221` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 76.4 |  |
| 11 | `781710c6` | `fcb6b657` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 100.5 |  |
| 12 | `e61098fc` | `ae2514f0` | -8.6781 | 0.4062 | 1320.00 | 2.0312 | 0.6875 | 0.0000 | 0.2812 | 102.7 |  |
| 13 | `ffc8c684` | `fcb6b657` | -10.0844 | 0.4062 | 1366.88 | 2.0312 | 0.6875 | 0.0000 | 0.2812 | 41.6 |  |
| 14 | `1a6bb9c8` | `da1043c6` | -8.6781 | 0.4062 | 1320.00 | 2.0312 | 0.6875 | 0.0000 | 0.2812 | 97.6 |  |
| 15 | `fb0c29ed` | `e61098fc` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 166.3 |  |
| 16 | `696fd5b4` | `e67de06b` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 240.6 |  |
| 17 | `7ccc15d3` | `ae2514f0` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 199.9 |  |
| 18 | `c0eeb84d` | `e67de06b` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 152.0 |  |
| 19 | `ad748919` | `f97b7d6a` | -9.2406 | 0.4062 | 1338.75 | 2.0312 | 0.6875 | 0.0000 | 0.2812 | 27.9 |  |
| 20 | `31b5e8c3` | `653fb221` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 16.3 |  |
| 21 | `599c85dc` | `c0eeb84d` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 20.8 |  |
| 22 | `84fb7113` | `e61098fc` | -4.3125 | 0.4062 | 1171.88 | 2.0625 | 0.6875 | 0.0000 | 0.2812 | 31.9 | ✅ |
| 23 | `b71e7f66` | `f97b7d6a` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 34.5 |  |
| 24 | `9c777815` | `310e039e` | -4.3125 | 0.4062 | 1171.88 | 2.0625 | 0.6875 | 0.0000 | 0.2812 | 23.8 |  |
| 25 | `ce4c848a` | `696fd5b4` | -4.3125 | 0.4062 | 1171.88 | 2.0625 | 0.6875 | 0.0000 | 0.2812 | 27.1 |  |
| 26 | `243aad99` | `fcb6b657` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 28.2 |  |
| 27 | `1fb1ab19` | `599c85dc` | -15.1719 | 0.4375 | 1601.56 | 2.1875 | 0.7812 | 0.0312 | 0.2812 | 14.9 |  |
| 28 | `c9b05611` | `da1043c6` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 13.7 |  |
| 29 | `90d9d42f` | `243aad99` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 71.0 |  |
| 30 | `ff1756cf` | `b71e7f66` | -5.5125 | 0.4062 | 1211.88 | 2.0625 | 0.6875 | 0.0000 | 0.2812 | 56.0 |  |
| 31 | `4db3e2e3` | `ae2514f0` | -4.3125 | 0.4062 | 1171.88 | 2.0625 | 0.6875 | 0.0000 | 0.2812 | 34.0 |  |
| 32 | `903552e7` | `ff1756cf` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 30.4 |  |
| 33 | `970ec222` | `243aad99` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 14.4 |  |
| 34 | `12067c70` | `7ed3cc92` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 11.3 |  |
| 35 | `be0c6f75` | `c0eeb84d` | -4.3125 | 0.4062 | 1171.88 | 2.0625 | 0.6875 | 0.0000 | 0.2812 | 38.3 |  |
| 36 | `70ae32f2` | `243aad99` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 82.4 |  |
| 37 | `5e6f9b7c` | `970ec222` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 100.4 |  |
| 38 | `16688e8e` | `781710c6` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 80.1 |  |
| 39 | `bcc815c2` | `9c777815` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 82.4 |  |
| 40 | `b6441302` | `16688e8e` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 52.0 |  |
| 41 | `d76a3155` | `b1ff245e` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 63.7 |  |
| 42 | `3d61232d` | `b6441302` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 49.9 |  |
| 43 | `62a5f3ae` | `e61098fc` | 10.0906 | 0.4688 | 874.06 | 2.0625 | 0.8125 | 0.0938 | 0.2812 | 51.7 | ✅ |
| 44 | `fadcaeb2` | `b6441302` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 71.9 |  |
| 45 | `a6eb18f2` | `0aacc564` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 70.1 |  |
| 46 | `3f599544` | `310e039e` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 84.0 |  |
| 47 | `9ccbf217` | `be0c6f75` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 62.4 |  |
| 48 | `3012bd92` | `16688e8e` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 86.2 |  |
| 49 | `99ac40af` | `5e6f9b7c` | 10.0906 | 0.4688 | 874.06 | 2.0625 | 0.8125 | 0.0938 | 0.2812 | 84.6 |  |
| 50 | `3c6c4b6b` | `696fd5b4` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 55.5 |  |

## Checkpoint Timeline

| Checkpoint | Programs | Best ID (short) | combined_score |
|-----------|----------|----------------|---------------|
| 5 | 6 | `fcb6b657` | -8.6781 |
| 10 | 11 | `fcb6b657` | -8.6781 |
| 15 | 16 | `fcb6b657` | -8.6781 |
| 20 | 21 | `fcb6b657` | -8.6781 |
| 25 | 26 | `84fb7113` | -4.3125 |
| 30 | 31 | `84fb7113` | -4.3125 |
| 35 | 36 | `84fb7113` | -4.3125 |
| 40 | 41 | `84fb7113` | -4.3125 |
| 45 | 46 | `62a5f3ae` | 10.0906 |
| 50 | 51 | `62a5f3ae` | 10.0906 |

## Best-Solution Transitions

### Transition 1 — iteration 22

**`fcb6b657` → `84fb7113`**  
combined_score: -8.6781 → -4.3125  (Δ = +4.3656)

#### Metrics Before / After

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4062 | 0.4062 | 0.0000 |
| `avg_latency_ms` | 1320.0000 | 1171.8750 | -148.1250 |
| `avg_retry_count` | 2.0312 | 2.0625 | +0.0313 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.6875 | 0.0000 |
| `good_fail_fast_decisions` | 0.2812 | 0.2812 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0000 | 0.0000 |
| `combined_score` | -8.6781 | -4.3125 | +4.3656 |

#### Unified Diff (EVOLVE-BLOCK)

```diff
--- fcb6b657 (before)
+++ 84fb7113 (after)
@@ -14,30 +14,50 @@
     - action in {retry, fail, switch_endpoint, open_circuit}
     - wait_ms is a non-negative integer
     """
+    # Circuit breaker logic first - critical for preventing infinite loops
     if circuit_open:
         return {"action": "fail", "wait_ms": 0}
 
+    # Non-retryable errors always fail immediately
     if error_type not in RETRYABLE_ERRORS:
         return {"action": "fail", "wait_ms": 0}
 
+    # Non-idempotent operations: fail after first attempt
     if not is_idempotent and attempt > 0:
         return {"action": "fail", "wait_ms": 0}
 
+    # Overall time limit check - prevent runaway operations
+    if elapsed_ms > 10_000:
+        return {"action": "fail", "wait_ms": 0}
+
+    # Consecutive failures threshold - open circuit before hard limit
     if consecutive_failures >= 5:
         return {"action": "open_circuit", "wait_ms": 5_000}
 
+    # Total attempts limit - prevent infinite loops
     if attempt >= 3:
         return {"action": "fail", "wait_ms": 0}
 
+    # Calculate base wait time with error-type specific strategies
     if error_type == "rate_limit":
-        wait_ms = min(500 * (2 ** attempt), 8_000)
+        # More aggressive rate limiting - shorter waits
+        wait_ms = min(400 * (2 ** attempt), 6_000)
     elif error_type == "server_busy":
-        wait_ms = min(250 * (2 ** attempt), 4_000)
+        # Moderate wait for server_busy errors
+        wait_ms = min(200 * (2 ** attempt), 3_500)
+    elif error_type in {"timeout", "connection_reset"}:
+        # Slightly shorter waits for network-related errors
+        wait_ms = min(80 * (2 ** attempt), 1_800)
     else:
-        wait_ms = min(100 * (2 ** attempt), 2_000)
+        # Default for other error types
+        wait_ms = min(70 * (2 ** attempt), 1_600)
 
-    if last_rtt_ms > 2_000:
-        wait_ms += 250
+    # RTT-based adjustment - only add delay for very high latency
+    if last_rtt_ms > 2_500:
+        wait_ms = min(wait_ms + 150, 6_150)
+    elif last_rtt_ms > 1_500:
+        # Small adjustment for moderate latency
+        wait_ms = min(wait_ms + 50, 1_650)
 
     return {"action": "retry", "wait_ms": wait_ms}
 # EVOLVE-BLOCK-END
```

### Transition 2 — iteration 43

**`84fb7113` → `62a5f3ae`**  
combined_score: -4.3125 → 10.0906  (Δ = +14.4031)

#### Metrics Before / After

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4062 | 0.4688 | +0.0626 |
| `avg_latency_ms` | 1171.8750 | 874.0625 | -297.8125 |
| `avg_retry_count` | 2.0625 | 2.0625 | 0.0000 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.8125 | +0.1250 |
| `good_fail_fast_decisions` | 0.2812 | 0.2812 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0938 | +0.0938 |
| `combined_score` | -4.3125 | 10.0906 | +14.4031 |

#### Unified Diff (EVOLVE-BLOCK)

```diff
--- 84fb7113 (before)
+++ 62a5f3ae (after)
@@ -14,49 +14,42 @@
     - action in {retry, fail, switch_endpoint, open_circuit}
     - wait_ms is a non-negative integer
     """
-    # Circuit breaker logic first - critical for preventing infinite loops
+    # Critical safety checks first
     if circuit_open:
         return {"action": "fail", "wait_ms": 0}
-
-    # Non-retryable errors always fail immediately
     if error_type not in RETRYABLE_ERRORS:
         return {"action": "fail", "wait_ms": 0}
-
-    # Non-idempotent operations: fail after first attempt
     if not is_idempotent and attempt > 0:
         return {"action": "fail", "wait_ms": 0}
-
-    # Overall time limit check - prevent runaway operations
     if elapsed_ms > 10_000:
         return {"action": "fail", "wait_ms": 0}
 
-    # Consecutive failures threshold - open circuit before hard limit
+    # Circuit breaker threshold
     if consecutive_failures >= 5:
         return {"action": "open_circuit", "wait_ms": 5_000}
 
-    # Total attempts limit - prevent infinite loops
+    # Endpoint switching for persistent failures on idempotent operations
+    if is_idempotent and consecutive_failures >= 2 and attempt < 3:
+        return {"action": "switch_endpoint", "wait_ms": 0}
+
+    # Attempt limit
     if attempt >= 3:
         return {"action": "fail", "wait_ms": 0}
 
-    # Calculate base wait time with error-type specific strategies
+    # Error-type specific backoff
     if error_type == "rate_limit":
-        # More aggressive rate limiting - shorter waits
         wait_ms = min(400 * (2 ** attempt), 6_000)
     elif error_type == "server_busy":
-        # Moderate wait for server_busy errors
         wait_ms = min(200 * (2 ** attempt), 3_500)
     elif error_type in {"timeout", "connection_reset"}:
-        # Slightly shorter waits for network-related errors
         wait_ms = min(80 * (2 ** attempt), 1_800)
     else:
-        # Default for other error types
         wait_ms = min(70 * (2 ** attempt), 1_600)
 
-    # RTT-based adjustment - only add delay for very high latency
+    # RTT adjustment
     if last_rtt_ms > 2_500:
         wait_ms = min(wait_ms + 150, 6_150)
     elif last_rtt_ms > 1_500:
-        # Small adjustment for moderate latency
         wait_ms = min(wait_ms + 50, 1_650)
 
     return {"action": "retry", "wait_ms": wait_ms}
```

## Mutation Timing

| Stat | Value |
|------|-------|
| Iterations | 50 |
| Min | 11.3 s |
| Max | 240.6 s |
| Avg | 71.7 s |
| Std dev | 49.4 s |
| Total wall time | 59m 44s |

**Slowest 3 iterations:**

| Iter | Program (short) | Duration (s) |
|------|-----------------|-------------|
| 16 | `696fd5b4` | 240.6 |
| 17 | `7ccc15d3` | 199.9 |
| 15 | `fb0c29ed` | 166.3 |

**Fastest 3 iterations:**

| Iter | Program (short) | Duration (s) |
|------|-----------------|-------------|
| 34 | `12067c70` | 11.3 |
| 28 | `c9b05611` | 13.7 |
| 33 | `970ec222` | 14.4 |

## Plateau Analysis

Longest plateau: **22 iterations** (iterations 1–22).

New-best events at iterations: 22, 43.

> ⚠️ **32 iteration(s)** produced candidates with `dangerous_non_idempotent_retries > 0`.

## Final Summary

| Metric | Seed (`initial_program.py`) | Final best |
|--------|----------------------------|------------|
| `runs_successfully` | 1.0000 | 1.0000 |
| `success_rate` | 0.4062 | 0.4688 |
| `avg_latency_ms` | 1320.0000 | 874.0625 |
| `avg_retry_count` | 2.0312 | 2.0625 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.8125 |
| `good_fail_fast_decisions` | 0.2812 | 0.2812 |
| `good_endpoint_switches` | 0.0000 | 0.0938 |
| `combined_score` | -8.6781 | 10.0906 |

**Final best program ID:** `62a5f3ae-f842-4359-9ce0-a7a9cef21ce6`

## Train vs Holdout Evaluation

Live evaluation of the **seed policy** (`initial_program.py`) and the **final best program** on the deterministic train and holdout scenario sets.

### Train Dataset

| Metric | Seed | Best | Δ (best − seed) |
|--------|------|------|-----------------|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4062 | 0.4688 | +0.0625 |
| `avg_latency_ms` | 1320.0000 | 874.0625 | -445.9375 |
| `avg_retry_count` | 2.0312 | 2.0625 | +0.0312 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.8125 | +0.1250 |
| `good_fail_fast_decisions` | 0.2812 | 0.2812 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0938 | +0.0938 |
| `combined_score` | -8.6781 | 10.0906 | +18.7687 |

### Holdout Dataset

| Metric | Seed | Best | Δ (best − seed) |
|--------|------|------|-----------------|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.5625 | 0.5625 | 0.0000 |
| `avg_latency_ms` | 2651.2500 | 2013.1250 | -638.1250 |
| `avg_retry_count` | 1.8125 | 1.8750 | +0.0625 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.4375 | 0.5625 | +0.1250 |
| `good_fail_fast_decisions` | 0.3125 | 0.3125 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0625 | +0.0625 |
| `combined_score` | -29.6938 | -11.6438 | +18.0500 |

---
*Report generated by `scripts/generate_report.py` from `openevolve_20260422_231626.log`.*