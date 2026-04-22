# Evolution Progress Report

**Log file:** `openevolve_20260422_223547.log`  
**Start:** 2026-04-22 22:35:47  **End:** 2026-04-22 23:07:46  
**Model:** `gemma4:31b-cloud`  **Seed:** 42  
**Iterations:** 50  **New-best events:** 4  
**Score:** -8.6781 → 8.5281  (Δ = +17.2062)

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
| `openevolve_output/logs/openevolve_20260422_223547.log` | Full run log |
| `openevolve_output/best/best_program.py` | Final best policy |
| `openevolve_output/best/best_program_info.json` | Final best metadata |
| `openevolve_output/checkpoints/checkpoint_5/` | 6 programs, best=-8.6781 |
| `openevolve_output/checkpoints/checkpoint_10/` | 11 programs, best=-7.0563 |
| `openevolve_output/checkpoints/checkpoint_15/` | 16 programs, best=-7.0563 |
| `openevolve_output/checkpoints/checkpoint_20/` | 21 programs, best=6.1844 |
| `openevolve_output/checkpoints/checkpoint_25/` | 26 programs, best=6.1844 |
| `openevolve_output/checkpoints/checkpoint_30/` | 31 programs, best=6.1844 |
| `openevolve_output/checkpoints/checkpoint_35/` | 36 programs, best=6.1844 |
| `openevolve_output/checkpoints/checkpoint_40/` | 41 programs, best=6.1844 |
| `openevolve_output/checkpoints/checkpoint_45/` | 46 programs, best=8.5281 |
| `openevolve_output/checkpoints/checkpoint_50/` | 51 programs, best=8.5281 |

## Iteration Timeline

| Iter | Program (short) | Parent (short) | combined_score | success_rate | avg_latency_ms | avg_retry_count | useless_retries | good_switches | fail_fast | dur_s | 🌟 |
|------|-----------------|----------------|---------------|-------------|----------------|----------------|----------------|--------------|-----------|-------|-----|
| 1 | `4d7a0d8e` | `be188e6c` | -8.8906 | 0.4688 | 1501.56 | 1.8750 | 0.8438 | 0.0312 | 0.2812 | 24.1 |  |
| 2 | `bf484503` | `be188e6c` | -45.8844 | 0.4375 | 2683.12 | 1.9062 | 0.6875 | 0.0000 | 0.3125 | 20.6 |  |
| 3 | `7d2ef17a` | `be188e6c` | -9.8281 | 0.4688 | 1532.81 | 1.8750 | 0.8438 | 0.0312 | 0.2812 | 22.2 |  |
| 4 | `41d84bfa` | `4d7a0d8e` | -11.7969 | 0.4688 | 1559.38 | 1.8438 | 1.0000 | 0.0938 | 0.2812 | 30.1 |  |
| 5 | `f8fea41b` | `4d7a0d8e` | -15.3594 | 0.4688 | 1717.19 | 1.8750 | 0.8438 | 0.0312 | 0.2812 | 79.0 |  |
| 6 | `3aa3c9dc` | `4d7a0d8e` | -18.0281 | 0.4688 | 1772.81 | 1.8750 | 1.0000 | 0.0938 | 0.3125 | 26.3 |  |
| 7 | `a4744982` | `4d7a0d8e` | -7.0563 | 0.4688 | 1398.75 | 1.8750 | 1.0000 | 0.0938 | 0.2812 | 29.9 | ✅ |
| 8 | `95874aaf` | `bf484503` | -9.4187 | 0.4688 | 1477.50 | 1.8750 | 1.0000 | 0.0938 | 0.2812 | 23.9 |  |
| 9 | `72e70458` | `41d84bfa` | -7.0563 | 0.4688 | 1398.75 | 1.8750 | 1.0000 | 0.0938 | 0.2812 | 26.2 |  |
| 10 | `26a99856` | `be188e6c` | -7.0563 | 0.4688 | 1398.75 | 1.8750 | 1.0000 | 0.0938 | 0.2812 | 93.1 |  |
| 11 | `39ab167f` | `a4744982` | -7.0563 | 0.4688 | 1398.75 | 1.8750 | 1.0000 | 0.0938 | 0.2812 | 88.4 |  |
| 12 | `0b96cad3` | `95874aaf` | -7.0563 | 0.4688 | 1398.75 | 1.8750 | 1.0000 | 0.0938 | 0.2812 | 31.2 |  |
| 13 | `bc523a81` | `39ab167f` | -9.8562 | 0.4688 | 1494.69 | 1.8438 | 1.0000 | 0.0938 | 0.2812 | 24.6 |  |
| 14 | `7e285155` | `72e70458` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 26.9 |  |
| 15 | `e33856f0` | `bc523a81` | -7.0563 | 0.4688 | 1398.75 | 1.8750 | 1.0000 | 0.0938 | 0.2812 | 52.1 |  |
| 16 | `b487cc41` | `7d2ef17a` | -7.0563 | 0.4688 | 1398.75 | 1.8750 | 1.0000 | 0.0938 | 0.2812 | 24.4 |  |
| 17 | `910a3a93` | `0b96cad3` | 5.6594 | 0.4688 | 1154.06 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 71.1 | ✅ |
| 18 | `807e910a` | `b487cc41` | -6.8563 | 0.4688 | 1290.00 | 1.8125 | 1.3125 | 0.1250 | 0.2500 | 26.6 |  |
| 19 | `75610632` | `910a3a93` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 23.9 | ✅ |
| 20 | `fc829212` | `0b96cad3` | 5.6594 | 0.4688 | 1154.06 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 30.2 |  |
| 21 | `64cb86d2` | `3aa3c9dc` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 68.9 |  |
| 22 | `bae71774` | `fc829212` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 55.4 |  |
| 23 | `bba334d8` | `3aa3c9dc` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 26.9 |  |
| 24 | `b4a479e0` | `95874aaf` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 42.1 |  |
| 25 | `26f2884f` | `bf484503` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 26.9 |  |
| 26 | `fa9ef3d7` | `b4a479e0` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 37.4 |  |
| 27 | `6ab7f82b` | `b487cc41` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 28.0 |  |
| 28 | `296c432a` | `bba334d8` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 90.6 |  |
| 29 | `448c46a8` | `bba334d8` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 30.6 |  |
| 30 | `dec64859` | `f8fea41b` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 29.5 |  |
| 31 | `e8709bea` | `fa9ef3d7` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 67.7 |  |
| 32 | `78c59fa7` | `bba334d8` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 26.6 |  |
| 33 | `542bd7d2` | `bf484503` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 40.3 |  |
| 34 | `bf065f0c` | `3aa3c9dc` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 53.8 |  |
| 35 | `54e1623f` | `6ab7f82b` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 39.7 |  |
| 36 | `8174ec0f` | `bba334d8` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 42.8 |  |
| 37 | `f8e0df62` | `3aa3c9dc` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 45.6 |  |
| 38 | `9f656aed` | `b4a479e0` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 20.0 |  |
| 39 | `c1473c78` | `54e1623f` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 17.6 |  |
| 40 | `6ebdf116` | `bc523a81` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 21.4 |  |
| 41 | `23d3d40a` | `f8fea41b` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 65.4 |  |
| 42 | `b8a8396f` | `fa9ef3d7` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 17.4 |  |
| 43 | `3825db8f` | `95874aaf` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 19.1 |  |
| 44 | `2e16423a` | `296c432a` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 26.8 |  |
| 45 | `6be9c626` | `9f656aed` | 8.5281 | 0.4688 | 1058.44 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 35.7 | ✅ |
| 46 | `0cb17e12` | `41d84bfa` | 6.1844 | 0.4688 | 1136.56 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 22.5 |  |
| 47 | `a1088726` | `4d7a0d8e` | 8.5281 | 0.4688 | 1058.44 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 29.7 |  |
| 48 | `cdba9d2f` | `26f2884f` | 8.5281 | 0.4688 | 1058.44 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 36.2 |  |
| 49 | `66c9adfd` | `a4744982` | -1.00e+09 | 0.0000 | 999999.00 | 999.0000 | 999.0000 | 0.0000 | 0.0000 | 43.0 |  |
| 50 | `072df383` | `39ab167f` | 8.5281 | 0.4688 | 1058.44 | 1.5000 | 0.6562 | 0.0938 | 0.4062 | 34.9 |  |

## Checkpoint Timeline

| Checkpoint | Programs | Best ID (short) | combined_score |
|-----------|----------|----------------|---------------|
| 5 | 6 | `be188e6c` | -8.6781 |
| 10 | 11 | `a4744982` | -7.0563 |
| 15 | 16 | `a4744982` | -7.0563 |
| 20 | 21 | `75610632` | 6.1844 |
| 25 | 26 | `75610632` | 6.1844 |
| 30 | 31 | `75610632` | 6.1844 |
| 35 | 36 | `75610632` | 6.1844 |
| 40 | 41 | `75610632` | 6.1844 |
| 45 | 46 | `6be9c626` | 8.5281 |
| 50 | 51 | `6be9c626` | 8.5281 |

## Best-Solution Transitions

### Transition 1 — iteration 7

**`be188e6c` → `a4744982`**  
combined_score: -8.6781 → -7.0563  (Δ = +1.6219)

#### Metrics Before / After

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4062 | 0.4688 | +0.0626 |
| `avg_latency_ms` | 1320.0000 | 1398.7500 | +78.7500 |
| `avg_retry_count` | 2.0312 | 1.8750 | -0.1562 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 1.0000 | +0.3125 |
| `good_fail_fast_decisions` | 0.2812 | 0.2812 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0938 | +0.0938 |
| `combined_score` | -8.6781 | -7.0563 | +1.6218 |

#### Unified Diff (EVOLVE-BLOCK)

```diff
--- be188e6c (before)
+++ a4744982 (after)
@@ -10,9 +10,9 @@
 ) -> Dict[str, int | str]:
     """Return the next retry-control action.
 
-    Contract:
-    - action in {retry, fail, switch_endpoint, open_circuit}
-    - wait_ms is a non-negative integer
+    This version optimizes for higher success rates by expanding the 
+    endpoint-switching criteria and refining the backoff timing to be 
+    more aggressive on transient errors while patient with rate limits.
     """
     if circuit_open:
         return {"action": "fail", "wait_ms": 0}
@@ -20,24 +20,40 @@
     if error_type not in RETRYABLE_ERRORS:
         return {"action": "fail", "wait_ms": 0}
 
+    # Safety: No retries for non-idempotent requests after the first failure
     if not is_idempotent and attempt > 0:
         return {"action": "fail", "wait_ms": 0}
 
-    if consecutive_failures >= 5:
+    # Circuit breaker for high failure streaks
+    if consecutive_failures >= 4:
         return {"action": "open_circuit", "wait_ms": 5_000}
 
+    # Fail fast to avoid excessive latency
     if attempt >= 3:
         return {"action": "fail", "wait_ms": 0}
 
+    # Strategic Endpoint Switching:
+    # Switch on network-level errors to bypass localized infrastructure issues.
+    # Include 'temporary_disconnect' and 'slow_response' as triggers.
+    switch_triggers = {"bad_gateway", "connection_reset", "timeout", "temporary_disconnect", "slow_response"}
+    if error_type in switch_triggers and attempt >= 1:
+        return {"action": "switch_endpoint", "wait_ms": 150}
+
+    # Differentiated Backoff
     if error_type == "rate_limit":
-        wait_ms = min(500 * (2 ** attempt), 8_000)
+        # Rate limits require longer, more stable pauses
+        wait_ms = 1200 * (2 ** attempt)
     elif error_type == "server_busy":
-        wait_ms = min(250 * (2 ** attempt), 4_000)
+        # Server load is usually transient
+        wait_ms = 600 * (2 ** attempt)
     else:
-        wait_ms = min(100 * (2 ** attempt), 2_000)
+        # General network errors use a tighter backoff for lower latency
+        wait_ms = 200 * (2 ** attempt)
 
-    if last_rtt_ms > 2_000:
-        wait_ms += 250
+    # Dynamic latency adjustment: 
+    # If RTT is high, we add a penalty to avoid congesting the pipe
+    if last_rtt_ms > 1200:
+        wait_ms += 300
 
-    return {"action": "retry", "wait_ms": wait_ms}
+    return {"action": "retry", "wait_ms": min(wait_ms, 10_000)}
 # EVOLVE-BLOCK-END
```

### Transition 2 — iteration 17

**`a4744982` → `910a3a93`**  
combined_score: -7.0563 → 5.6594  (Δ = +12.7156)

#### Metrics Before / After

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4688 | 0.4688 | 0.0000 |
| `avg_latency_ms` | 1398.7500 | 1154.0625 | -244.6875 |
| `avg_retry_count` | 1.8750 | 1.5000 | -0.3750 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 1.0000 | 0.6562 | -0.3438 |
| `good_fail_fast_decisions` | 0.2812 | 0.4062 | +0.1250 |
| `good_endpoint_switches` | 0.0938 | 0.0938 | 0.0000 |
| `combined_score` | -7.0563 | 5.6594 | +12.7157 |

#### Unified Diff (EVOLVE-BLOCK)

```diff
--- a4744982 (before)
+++ 910a3a93 (after)
@@ -10,9 +10,8 @@
 ) -> Dict[str, int | str]:
     """Return the next retry-control action.
 
-    This version optimizes for higher success rates by expanding the 
-    endpoint-switching criteria and refining the backoff timing to be 
-    more aggressive on transient errors while patient with rate limits.
+    Optimized to reduce 'useless_retries' and improve 'good_fail_fast_decisions'
+    by tightening the retry budget and refining the endpoint switch trigger.
     """
     if circuit_open:
         return {"action": "fail", "wait_ms": 0}
@@ -20,40 +19,39 @@
     if error_type not in RETRYABLE_ERRORS:
         return {"action": "fail", "wait_ms": 0}
 
-    # Safety: No retries for non-idempotent requests after the first failure
+    # Strict safety for non-idempotent requests
     if not is_idempotent and attempt > 0:
         return {"action": "fail", "wait_ms": 0}
 
-    # Circuit breaker for high failure streaks
-    if consecutive_failures >= 4:
-        return {"action": "open_circuit", "wait_ms": 5_000}
+    # Circuit breaker: Open circuit earlier if failure streak is high
+    if consecutive_failures >= 3:
+        return {"action": "open_circuit", "wait_ms": 3000}
 
-    # Fail fast to avoid excessive latency
-    if attempt >= 3:
+    # Fail fast: Reduce max attempts to 2 to minimize useless retries and latency
+    if attempt >= 2:
         return {"action": "fail", "wait_ms": 0}
 
     # Strategic Endpoint Switching:
-    # Switch on network-level errors to bypass localized infrastructure issues.
-    # Include 'temporary_disconnect' and 'slow_response' as triggers.
-    switch_triggers = {"bad_gateway", "connection_reset", "timeout", "temporary_disconnect", "slow_response"}
-    if error_type in switch_triggers and attempt >= 1:
-        return {"action": "switch_endpoint", "wait_ms": 150}
+    # Switch on the first retry (attempt 1) for network-level errors.
+    # We prioritize switching over retrying the same endpoint.
+    switch_triggers = {"bad_gateway", "connection_reset", "timeout", "temporary_disconnect"}
+    if attempt >= 1 and error_type in switch_triggers:
+        return {"action": "switch_endpoint", "wait_ms": 100}
 
-    # Differentiated Backoff
+    # Tiered Backoff Strategy
     if error_type == "rate_limit":
-        # Rate limits require longer, more stable pauses
-        wait_ms = 1200 * (2 ** attempt)
+        # Rate limits need significant breathing room
+        wait_ms = 1500 * (2 ** attempt)
     elif error_type == "server_busy":
-        # Server load is usually transient
-        wait_ms = 600 * (2 ** attempt)
+        # Server load is transient
+        wait_ms = 800 * (2 ** attempt)
     else:
-        # General network errors use a tighter backoff for lower latency
-        wait_ms = 200 * (2 ** attempt)
+        # Low latency backoff for general network glitches
+        wait_ms = 300 * (2 ** attempt)
 
-    # Dynamic latency adjustment: 
-    # If RTT is high, we add a penalty to avoid congesting the pipe
-    if last_rtt_ms > 1200:
-        wait_ms += 300
+    # RTT-based congestion avoidance
+    if last_rtt_ms > 1000:
+        wait_ms += 200
 
     return {"action": "retry", "wait_ms": min(wait_ms, 10_000)}
 # EVOLVE-BLOCK-END
```

### Transition 3 — iteration 19

**`910a3a93` → `75610632`**  
combined_score: 5.6594 → 6.1844  (Δ = +0.5250)

#### Metrics Before / After

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4688 | 0.4688 | 0.0000 |
| `avg_latency_ms` | 1154.0625 | 1136.5625 | -17.5000 |
| `avg_retry_count` | 1.5000 | 1.5000 | 0.0000 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.6562 | 0.6562 | 0.0000 |
| `good_fail_fast_decisions` | 0.4062 | 0.4062 | 0.0000 |
| `good_endpoint_switches` | 0.0938 | 0.0938 | 0.0000 |
| `combined_score` | 5.6594 | 6.1844 | +0.5250 |

#### Unified Diff (EVOLVE-BLOCK)

```diff
--- 910a3a93 (before)
+++ 75610632 (after)
@@ -10,8 +10,8 @@
 ) -> Dict[str, int | str]:
     """Return the next retry-control action.
 
-    Optimized to reduce 'useless_retries' and improve 'good_fail_fast_decisions'
-    by tightening the retry budget and refining the endpoint switch trigger.
+    Refined to maximize fitness by aggressively pruning useless retries
+    and optimizing endpoint switching for network-level failures.
     """
     if circuit_open:
         return {"action": "fail", "wait_ms": 0}
@@ -19,37 +19,37 @@
     if error_type not in RETRYABLE_ERRORS:
         return {"action": "fail", "wait_ms": 0}
 
-    # Strict safety for non-idempotent requests
+    # Safety: Never retry non-idempotent requests
     if not is_idempotent and attempt > 0:
         return {"action": "fail", "wait_ms": 0}
 
-    # Circuit breaker: Open circuit earlier if failure streak is high
+    # Circuit breaker: Trigger on a moderate streak to prevent cascading failure
     if consecutive_failures >= 3:
         return {"action": "open_circuit", "wait_ms": 3000}
 
-    # Fail fast: Reduce max attempts to 2 to minimize useless retries and latency
+    # Fail fast: Limit to 2 attempts total to minimize 'useless_retries' and latency
     if attempt >= 2:
         return {"action": "fail", "wait_ms": 0}
 
     # Strategic Endpoint Switching:
-    # Switch on the first retry (attempt 1) for network-level errors.
-    # We prioritize switching over retrying the same endpoint.
-    switch_triggers = {"bad_gateway", "connection_reset", "timeout", "temporary_disconnect"}
+    # Switch on the first retry (attempt 1) for infrastructure-level errors.
+    # This bypasses bad nodes quickly.
+    switch_triggers = {"bad_gateway", "connection_reset", "timeout", "temporary_disconnect", "slow_response"}
     if attempt >= 1 and error_type in switch_triggers:
         return {"action": "switch_endpoint", "wait_ms": 100}
 
-    # Tiered Backoff Strategy
+    # Tiered Exponential Backoff
     if error_type == "rate_limit":
-        # Rate limits need significant breathing room
+        # Rate limits need substantial time to reset
         wait_ms = 1500 * (2 ** attempt)
     elif error_type == "server_busy":
-        # Server load is transient
+        # Server load is transient but needs a small gap
         wait_ms = 800 * (2 ** attempt)
     else:
-        # Low latency backoff for general network glitches
+        # Fast recovery for transient network glitches
         wait_ms = 300 * (2 ** attempt)
 
-    # RTT-based congestion avoidance
+    # Congestion avoidance: Add delay if the network is showing high latency
     if last_rtt_ms > 1000:
         wait_ms += 200
```

### Transition 4 — iteration 45

**`75610632` → `6be9c626`**  
combined_score: 6.1844 → 8.5281  (Δ = +2.3437)

#### Metrics Before / After

| Metric | Before | After | Δ |
|--------|--------|-------|---|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4688 | 0.4688 | 0.0000 |
| `avg_latency_ms` | 1136.5625 | 1058.4375 | -78.1250 |
| `avg_retry_count` | 1.5000 | 1.5000 | 0.0000 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.6562 | 0.6562 | 0.0000 |
| `good_fail_fast_decisions` | 0.4062 | 0.4062 | 0.0000 |
| `good_endpoint_switches` | 0.0938 | 0.0938 | 0.0000 |
| `combined_score` | 6.1844 | 8.5281 | +2.3437 |

#### Unified Diff (EVOLVE-BLOCK)

```diff
--- 75610632 (before)
+++ 6be9c626 (after)
@@ -8,50 +8,52 @@
     is_idempotent: bool,
     circuit_open: bool,
 ) -> Dict[str, int | str]:
-    """Return the next retry-control action.
-
-    Refined to maximize fitness by aggressively pruning useless retries
-    and optimizing endpoint switching for network-level failures.
     """
-    if circuit_open:
+    Optimized retry policy to maximize fitness.
+    
+    Improvements:
+    1. Aggressive Fail-Fast: Limit attempts strictly to 2 (0, 1) to minimize useless_retries.
+    2. High-Precision Switching: Switch endpoints immediately on attempt 1 for network errors.
+    3. Idempotency Guard: Absolute zero tolerance for non-idempotent retries.
+    4. Rapid Circuit Breaking: Open circuit on 3 consecutive failures.
+    5. Refined Backoff: Tightened wait times to reduce latency while maintaining success.
+    """
+    # Immediate fail for circuit open or non-retryable errors
+    if circuit_open or error_type not in RETRYABLE_ERRORS:
         return {"action": "fail", "wait_ms": 0}
 
-    if error_type not in RETRYABLE_ERRORS:
-        return {"action": "fail", "wait_ms": 0}
-
-    # Safety: Never retry non-idempotent requests
+    # Safety: Non-idempotent requests must never be retried
     if not is_idempotent and attempt > 0:
         return {"action": "fail", "wait_ms": 0}
 
-    # Circuit breaker: Trigger on a moderate streak to prevent cascading failure
+    # Circuit breaker: Trigger rapidly on failure streaks
     if consecutive_failures >= 3:
         return {"action": "open_circuit", "wait_ms": 3000}
 
-    # Fail fast: Limit to 2 attempts total to minimize 'useless_retries' and latency
+    # Fail fast: Cap at 2 attempts (0 and 1) to optimize latency and useless_retries
     if attempt >= 2:
         return {"action": "fail", "wait_ms": 0}
 
     # Strategic Endpoint Switching:
-    # Switch on the first retry (attempt 1) for infrastructure-level errors.
-    # This bypasses bad nodes quickly.
+    # Switch on the first retry (attempt 1) for infrastructure-level failures to bypass bad nodes.
     switch_triggers = {"bad_gateway", "connection_reset", "timeout", "temporary_disconnect", "slow_response"}
     if attempt >= 1 and error_type in switch_triggers:
         return {"action": "switch_endpoint", "wait_ms": 100}
 
-    # Tiered Exponential Backoff
+    # Tiered Backoff based on error type
     if error_type == "rate_limit":
-        # Rate limits need substantial time to reset
-        wait_ms = 1500 * (2 ** attempt)
+        # Rate limits need a significant window to reset
+        wait_ms = 1400 * (2 ** attempt)
     elif error_type == "server_busy":
-        # Server load is transient but needs a small gap
-        wait_ms = 800 * (2 ** attempt)
+        # Server load is transient
+        wait_ms = 700 * (2 ** attempt)
     else:
         # Fast recovery for transient network glitches
-        wait_ms = 300 * (2 ** attempt)
+        wait_ms = 250 * (2 ** attempt)
 
-    # Congestion avoidance: Add delay if the network is showing high latency
+    # Congestion avoidance: Add delay if network RTT is high
     if last_rtt_ms > 1000:
-        wait_ms += 200
+        wait_ms += 150
 
     return {"action": "retry", "wait_ms": min(wait_ms, 10_000)}
 # EVOLVE-BLOCK-END
```

## Mutation Timing

| Stat | Value |
|------|-------|
| Iterations | 50 |
| Min | 17.4 s |
| Max | 93.1 s |
| Avg | 38.3 s |
| Std dev | 19.9 s |
| Total wall time | 31m 57s |

**Slowest 3 iterations:**

| Iter | Program (short) | Duration (s) |
|------|-----------------|-------------|
| 10 | `26a99856` | 93.1 |
| 28 | `296c432a` | 90.6 |
| 11 | `39ab167f` | 88.4 |

**Fastest 3 iterations:**

| Iter | Program (short) | Duration (s) |
|------|-----------------|-------------|
| 42 | `b8a8396f` | 17.4 |
| 39 | `c1473c78` | 17.6 |
| 43 | `3825db8f` | 19.1 |

## Plateau Analysis

Longest plateau: **26 iterations** (iterations 20–45).

New-best events at iterations: 7, 17, 19, 45.

> ⚠️ **4 iteration(s)** produced candidates with `dangerous_non_idempotent_retries > 0`.

## Final Summary

| Metric | Seed (`initial_program.py`) | Final best |
|--------|----------------------------|------------|
| `runs_successfully` | 1.0000 | 1.0000 |
| `success_rate` | 0.4062 | 0.4688 |
| `avg_latency_ms` | 1320.0000 | 1058.4375 |
| `avg_retry_count` | 2.0312 | 1.5000 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.6562 |
| `good_fail_fast_decisions` | 0.2812 | 0.4062 |
| `good_endpoint_switches` | 0.0000 | 0.0938 |
| `combined_score` | -8.6781 | 8.5281 |

**Final best program ID:** `6be9c626-d9b2-439f-a2e4-5b26470b25e9`

## Train vs Holdout Evaluation

Live evaluation of the **seed policy** (`initial_program.py`) and the **final best program** on the deterministic train and holdout scenario sets.

### Train Dataset

| Metric | Seed | Best | Δ (best − seed) |
|--------|------|------|-----------------|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.4062 | 0.4688 | +0.0625 |
| `avg_latency_ms` | 1320.0000 | 1058.4375 | -261.5625 |
| `avg_retry_count` | 2.0312 | 1.5000 | -0.5312 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.6875 | 0.6562 | -0.0312 |
| `good_fail_fast_decisions` | 0.2812 | 0.4062 | +0.1250 |
| `good_endpoint_switches` | 0.0000 | 0.0938 | +0.0938 |
| `combined_score` | -8.6781 | 8.5281 | +17.2062 |

### Holdout Dataset

| Metric | Seed | Best | Δ (best − seed) |
|--------|------|------|-----------------|
| `runs_successfully` | 1.0000 | 1.0000 | 0.0000 |
| `success_rate` | 0.5625 | 0.5625 | 0.0000 |
| `avg_latency_ms` | 2651.2500 | 2199.3750 | -451.8750 |
| `avg_retry_count` | 1.8125 | 1.3750 | -0.4375 |
| `dangerous_non_idempotent_retries` | 0.0000 | 0.0000 | 0.0000 |
| `useless_retries` | 0.4375 | 0.4375 | 0.0000 |
| `good_fail_fast_decisions` | 0.3125 | 0.3125 | 0.0000 |
| `good_endpoint_switches` | 0.0000 | 0.0000 | 0.0000 |
| `combined_score` | -29.6938 | -15.0437 | +14.6500 |

---
*Report generated by `scripts/generate_report.py` from `openevolve_20260422_223547.log`.*