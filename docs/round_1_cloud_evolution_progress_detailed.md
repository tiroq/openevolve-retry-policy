# Retry Policy Evolution - Full Detailed History

## Sources Read First

- openevolve_output/logs/openevolve_20260421_110550.log
- openevolve_output/best/best_program.py
- openevolve_output/best/best_program_info.json
- openevolve_output/checkpoints/checkpoint_*/best_program.py
- openevolve_output/checkpoints/checkpoint_*/best_program_info.json
- openevolve_output/checkpoints/checkpoint_*/programs/*.json
- initial_program.py

## Output Folder Inventory

- Total files in openevolve_output: 318
- Files in openevolve_output/best: 2
- Files in openevolve_output/logs: 1

### best folder

- best_program.py
- best_program_info.json

### logs folder

- openevolve_20260421_110550.log

### checkpoint program JSON counts

- checkpoint_5: 6
- checkpoint_10: 11
- checkpoint_15: 16
- checkpoint_20: 21
- checkpoint_25: 26
- checkpoint_30: 31
- checkpoint_35: 36
- checkpoint_40: 41
- checkpoint_45: 46
- checkpoint_50: 51

## Full Iteration Timeline (1-50)

| Iteration | Program ID | Parent ID | Duration(s) | combined_score | success_rate | avg_latency_ms | avg_retry_count | useless_retries | good_endpoint_switches |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 57e93334-be2b-455c-b98e-8bc43b90c6b7 | 61b091ad-3607-471b-acdd-ae0f6c285c27 | 20.23 | -2.3344 | 0.4375 | 1207.5000 | 2.0312 | 0.7188 | 0.0312 |
| 2 | 4a61a3b5-54f7-4843-9ee4-d38a92f6c93e | 61b091ad-3607-471b-acdd-ae0f6c285c27 | 9.47 | -11.6406 | 0.4688 | 1421.8750 | 2.0938 | 1.2188 | 0.0625 |
| 3 | e28a8b35-2562-4e57-a320-9d88ce94f2f3 | 57e93334-be2b-455c-b98e-8bc43b90c6b7 | 10.55 | -9.3250 | 0.4375 | 1357.1875 | 1.9062 | 1.0000 | 0.0312 |
| 4 | 42cda27a-c5f8-43c1-b9b0-4e4da19d2238 | 4a61a3b5-54f7-4843-9ee4-d38a92f6c93e | 20.06 | -10.7875 | 0.4375 | 1484.0625 | 1.9688 | 0.7500 | 0.0312 |
| 5 | b49caea0-f858-4a2c-9873-75d973cac79a | e28a8b35-2562-4e57-a320-9d88ce94f2f3 | 23.09 | 7.2594 | 0.4688 | 688.7500 | 2.0312 | 1.6250 | 0.1250 |
| 6 | e59beed2-1c26-478d-8156-67636e96a5ac | e28a8b35-2562-4e57-a320-9d88ce94f2f3 | 14.70 | 0.2313 | 0.4688 | 1027.1875 | 2.0312 | 1.2812 | 0.0625 |
| 7 | 66222e3f-bdb8-4248-9863-f7237f855975 | e28a8b35-2562-4e57-a320-9d88ce94f2f3 | 20.31 | 7.2594 | 0.4688 | 688.7500 | 2.0312 | 1.6250 | 0.1250 |
| 8 | 39cfe3ca-9629-4338-823a-f0da63eeb97f | e59beed2-1c26-478d-8156-67636e96a5ac | 20.76 | 9.0969 | 0.4688 | 627.5000 | 2.0312 | 1.6250 | 0.1250 |
| 9 | 8e3390ac-14e3-4c36-9dda-1f18ffdd6b45 | 61b091ad-3607-471b-acdd-ae0f6c285c27 | 13.12 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 10 | 0722c9c4-0f6b-4a8f-bdc5-5b202f5abfc3 | 39cfe3ca-9629-4338-823a-f0da63eeb97f | 23.11 | 9.9375 | 0.4688 | 604.6875 | 1.9688 | 1.6250 | 0.1250 |
| 11 | b713cf5b-c671-4f1b-8bb8-117f4f34c6f5 | 66222e3f-bdb8-4248-9863-f7237f855975 | 31.11 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 12 | ef0af7ea-9e6e-4c65-acad-47fd7fd0ccdc | 66222e3f-bdb8-4248-9863-f7237f855975 | 46.57 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 13 | b4de1653-0dc1-4ce7-a3ae-1122a120b0fe | 61b091ad-3607-471b-acdd-ae0f6c285c27 | 21.84 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 14 | aa685026-4b5d-4272-8fb2-0ea4f351769e | 39cfe3ca-9629-4338-823a-f0da63eeb97f | 11.63 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 15 | f2260fca-5908-465f-9e27-182059eb1481 | ef0af7ea-9e6e-4c65-acad-47fd7fd0ccdc | 18.95 | 4.6562 | 0.3750 | 306.2500 | 2.3125 | 2.0000 | 0.1250 |
| 16 | b5ad0854-aae2-464e-85fc-d2da2ba38671 | 57e93334-be2b-455c-b98e-8bc43b90c6b7 | 19.00 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 17 | af0f2535-2fd6-4c63-9e4b-3a1c57ae4a27 | aa685026-4b5d-4272-8fb2-0ea4f351769e | 24.04 | 7.3625 | 0.4688 | 650.9375 | 2.0938 | 1.6875 | 0.1250 |
| 18 | f45fb3a8-b24a-4c1a-bd59-530e0d077de3 | ef0af7ea-9e6e-4c65-acad-47fd7fd0ccdc | 24.55 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 19 | ca507019-a51a-42dd-9451-1670ec3fb979 | ef0af7ea-9e6e-4c65-acad-47fd7fd0ccdc | 43.68 | 0.9844 | 0.3438 | 275.0000 | 2.4062 | 2.1250 | 0.1250 |
| 20 | 625c20a0-9408-4492-b234-04e8d3092b1c | ef0af7ea-9e6e-4c65-acad-47fd7fd0ccdc | 37.15 | 8.2531 | 0.4688 | 621.2500 | 2.0938 | 1.6875 | 0.1250 |
| 21 | dad6df45-aac2-40e9-ba8b-ee3b7c8d01cb | 61b091ad-3607-471b-acdd-ae0f6c285c27 | 14.42 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 22 | aef62a23-8974-4922-9acb-885d1aef4308 | 0722c9c4-0f6b-4a8f-bdc5-5b202f5abfc3 | 24.28 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 23 | 8177f95b-4dbb-45ca-8afa-e7dd44e6cd1b | 57e93334-be2b-455c-b98e-8bc43b90c6b7 | 18.38 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 24 | 40f9e12b-78dc-41a5-b1e6-e7a9f6e64c55 | 625c20a0-9408-4492-b234-04e8d3092b1c | 44.61 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 25 | 5296c8b6-e39d-4191-9595-da6fdc809e36 | f45fb3a8-b24a-4c1a-bd59-530e0d077de3 | 20.83 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 26 | 2a61f0b2-4d4a-469e-a563-3e4f1dea1c6a | e59beed2-1c26-478d-8156-67636e96a5ac | 8.11 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 27 | d6be2574-b2a3-430b-9712-e1d0be6a7a74 | 8e3390ac-14e3-4c36-9dda-1f18ffdd6b45 | 42.78 | 8.0656 | 0.4688 | 627.5000 | 2.0938 | 1.6875 | 0.1250 |
| 28 | c583301c-3586-48de-9b33-19c513225d06 | 8e3390ac-14e3-4c36-9dda-1f18ffdd6b45 | 22.59 | 7.3625 | 0.4688 | 650.9375 | 2.0938 | 1.6875 | 0.1250 |
| 29 | b5ac6717-c4d7-4a69-842d-4669052f44ef | b713cf5b-c671-4f1b-8bb8-117f4f34c6f5 | 17.53 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 30 | 44a29f94-ad4d-49e9-b3e0-d27f92a3d30b | d6be2574-b2a3-430b-9712-e1d0be6a7a74 | 16.88 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 31 | 1cff160e-b671-46eb-8069-0eb749acb5cb | 8e3390ac-14e3-4c36-9dda-1f18ffdd6b45 | 23.60 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 32 | 64e9b00e-d9d8-4cc5-8180-bf55a99296dd | ef0af7ea-9e6e-4c65-acad-47fd7fd0ccdc | 16.83 | 8.7688 | 0.4688 | 604.0625 | 2.0938 | 1.6875 | 0.1250 |
| 33 | 4dca1957-bc03-417f-823e-0047d27deff6 | 5296c8b6-e39d-4191-9595-da6fdc809e36 | 15.34 | 3.0156 | 0.3750 | 360.9375 | 2.3125 | 2.0000 | 0.1250 |
| 34 | 73813cd4-6e22-4567-8502-558478df5e31 | e28a8b35-2562-4e57-a320-9d88ce94f2f3 | 21.62 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 35 | cba1333a-4361-4808-90e9-53e366b853c3 | aa685026-4b5d-4272-8fb2-0ea4f351769e | 37.66 | 5.3156 | 0.4375 | 575.9375 | 2.1875 | 1.7812 | 0.1250 |
| 36 | 5f78b247-a790-42d8-99f8-e39a674cb21a | b713cf5b-c671-4f1b-8bb8-117f4f34c6f5 | 21.92 | 7.3625 | 0.4688 | 650.9375 | 2.0938 | 1.6875 | 0.1250 |
| 37 | 56db6479-1fb0-4eff-add6-2c85d123fc5e | 4a61a3b5-54f7-4843-9ee4-d38a92f6c93e | 19.03 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 38 | a2977d27-0811-42ae-8627-6a5a73344d0d | af0f2535-2fd6-4c63-9e4b-3a1c57ae4a27 | 14.24 | 8.4406 | 0.4688 | 615.0000 | 2.0938 | 1.6875 | 0.1250 |
| 39 | 4a489c0e-6fc1-493c-924c-0ac7ab5627f2 | 42cda27a-c5f8-43c1-b9b0-4e4da19d2238 | 17.33 | 10.5500 | 0.4688 | 544.6875 | 2.0938 | 1.6875 | 0.1250 |
| 40 | f074cf4b-a91b-4d8e-94bc-c14a4c04c4cd | cba1333a-4361-4808-90e9-53e366b853c3 | 13.73 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 41 | f77abb78-428e-46ac-9319-1fad1a862add | a2977d27-0811-42ae-8627-6a5a73344d0d | 20.24 | 12.2844 | 0.4688 | 486.8750 | 2.0938 | 1.6875 | 0.1250 |
| 42 | 92519928-a3a4-483f-9f49-c9a6143f90b7 | f074cf4b-a91b-4d8e-94bc-c14a4c04c4cd | 13.94 | 7.3625 | 0.4688 | 650.9375 | 2.0938 | 1.6875 | 0.1250 |
| 43 | 3d3d1f24-2ed3-497e-b5e3-3b63084ee5dc | 1cff160e-b671-46eb-8069-0eb749acb5cb | 12.73 | 12.2844 | 0.4688 | 486.8750 | 2.0938 | 1.6875 | 0.1250 |
| 44 | bdc923ff-070f-4c1a-a973-1e3f1ae79bb2 | f45fb3a8-b24a-4c1a-bd59-530e0d077de3 | 13.55 | 12.2844 | 0.4688 | 486.8750 | 2.0938 | 1.6875 | 0.1250 |
| 45 | b65bcb64-591c-4226-89f4-604237bf8955 | d6be2574-b2a3-430b-9712-e1d0be6a7a74 | 10.56 | 12.2844 | 0.4688 | 486.8750 | 2.0938 | 1.6875 | 0.1250 |
| 46 | 838a1280-6092-4258-9c90-b7f072c93e81 | 8177f95b-4dbb-45ca-8afa-e7dd44e6cd1b | 19.02 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 47 | 1c5e80c1-adb4-4db3-aa2b-39eea758ef78 | 73813cd4-6e22-4567-8502-558478df5e31 | 10.37 | 12.2844 | 0.4688 | 486.8750 | 2.0938 | 1.6875 | 0.1250 |
| 48 | b66324c6-2337-49d7-a5c6-173a2ee3c434 | 39cfe3ca-9629-4338-823a-f0da63eeb97f | 10.34 | 10.8781 | 0.4688 | 533.7500 | 2.0938 | 1.6875 | 0.1250 |
| 49 | 55e730b0-680d-4ff1-9f48-2c946ff52291 | c583301c-3586-48de-9b33-19c513225d06 | 17.74 | 12.2844 | 0.4688 | 486.8750 | 2.0938 | 1.6875 | 0.1250 |
| 50 | 2160e87a-2f5c-4ed0-b9dc-8495da6d18af | 5296c8b6-e39d-4191-9595-da6fdc809e36 | 9.80 | 12.2844 | 0.4688 | 486.8750 | 2.0938 | 1.6875 | 0.1250 |

## Checkpoint Timeline

- Iteration 5: openevolve_output/checkpoints/checkpoint_5
- Iteration 10: openevolve_output/checkpoints/checkpoint_10
- Iteration 15: openevolve_output/checkpoints/checkpoint_15
- Iteration 20: openevolve_output/checkpoints/checkpoint_20
- Iteration 25: openevolve_output/checkpoints/checkpoint_25
- Iteration 30: openevolve_output/checkpoints/checkpoint_30
- Iteration 35: openevolve_output/checkpoints/checkpoint_35
- Iteration 40: openevolve_output/checkpoints/checkpoint_40
- Iteration 45: openevolve_output/checkpoints/checkpoint_45
- Iteration 50: openevolve_output/checkpoints/checkpoint_50

## Best Evolution Milestones (Step by Step)

### Step 1 - New Best at Iteration 1

- Transition: 61b091ad-3607-471b-acdd-ae0f6c285c27 -> 57e93334-be2b-455c-b98e-8bc43b90c6b7
- Score: -8.6781 -> -2.3344 (delta +6.3438)
- Metrics before/after:
  - success_rate: 0.4062 -> 0.4375
  - avg_latency_ms: 1320.0000 -> 1207.5000
  - avg_retry_count: 2.0312 -> 2.0312
  - useless_retries: 0.6875 -> 0.7188
  - good_endpoint_switches: 0.0000 -> 0.0312

```diff
--- 61b091ad
+++ 57e93334
@@ -26,9 +26,15 @@
    if consecutive_failures >= 5:
        return {"action": "open_circuit", "wait_ms": 5_000}
 
+    if consecutive_failures >= 2 and error_type in {"bad_gateway", "timeout"}:
+        return {"action": "switch_endpoint", "wait_ms": 0}
+
    if attempt >= 3:
        return {"action": "fail", "wait_ms": 0}
 
+    if last_rtt_ms > 5_000:
+        return {"action": "switch_endpoint", "wait_ms": 0}
+
    if error_type == "rate_limit":
        wait_ms = min(500 * (2 ** attempt), 8_000)
    elif error_type == "server_busy":
```

Explanation: The first improvement introduced conditional endpoint switching for repeated bad gateway/timeout and very high RTT. That immediately improved success_rate and reduced latency while preserving safety constraints.

### Step 2 - New Best at Iteration 5

- Transition: 57e93334-be2b-455c-b98e-8bc43b90c6b7 -> b49caea0-f858-4a2c-9873-75d973cac79a
- Score: -2.3344 -> 7.2594 (delta +9.5938)
- Metrics before/after:
  - success_rate: 0.4375 -> 0.4688
  - avg_latency_ms: 1207.5000 -> 688.7500
  - avg_retry_count: 2.0312 -> 2.0312
  - useless_retries: 0.7188 -> 1.6250
  - good_endpoint_switches: 0.0312 -> 0.1250

```diff
--- 57e93334
+++ b49caea0
@@ -26,24 +26,23 @@
    if consecutive_failures >= 5:
        return {"action": "open_circuit", "wait_ms": 5_000}
 
-    if consecutive_failures >= 2 and error_type in {"bad_gateway", "timeout"}:
+    # Switch endpoint on critical network errors or high latency
+    if error_type in {"bad_gateway", "timeout", "connection_reset", "temporary_disconnect"} or last_rtt_ms > 3_500:
        return {"action": "switch_endpoint", "wait_ms": 0}
 
-    if attempt >= 3:
+    if attempt >= 3 or elapsed_ms > 15_000:
        return {"action": "fail", "wait_ms": 0}
 
-    if last_rtt_ms > 5_000:
-        return {"action": "switch_endpoint", "wait_ms": 0}
-
    if error_type == "rate_limit":
-        wait_ms = min(500 * (2 ** attempt), 8_000)
+        wait_ms = min(600 * (2 ** attempt), 8_000)
    elif error_type == "server_busy":
-        wait_ms = min(250 * (2 ** attempt), 4_000)
+        wait_ms = min(400 * (2 ** attempt), 4_000)
    else:
-        wait_ms = min(100 * (2 ** attempt), 2_000)
+        wait_ms = min(200 * (2 ** attempt), 2_500)
 
+    # Add jitter/extra wait if RTT is creeping up
    if last_rtt_ms > 2_000:
-        wait_ms += 250
+        wait_ms += 300
```

Explanation: This step generalized endpoint switching and tuned waits, creating a major latency drop and a large fitness gain. It traded off higher useless retries for much better endpoint switch behavior and response time.

### Step 3 - New Best at Iteration 8

- Transition: b49caea0-f858-4a2c-9873-75d973cac79a -> 39cfe3ca-9629-4338-823a-f0da63eeb97f
- Score: 7.2594 -> 9.0969 (delta +1.8375)
- Metrics before/after:
  - success_rate: 0.4688 -> 0.4688
  - avg_latency_ms: 688.7500 -> 627.5000
  - avg_retry_count: 2.0312 -> 2.0312
  - useless_retries: 1.6250 -> 1.6250
  - good_endpoint_switches: 0.1250 -> 0.1250

```diff
--- b49caea0
+++ 39cfe3ca
@@ -27,14 +27,19 @@
        return {"action": "open_circuit", "wait_ms": 5_000}
 
    # Switch endpoint on critical network errors or high latency
-    if error_type in {"bad_gateway", "timeout", "connection_reset", "temporary_disconnect"} or last_rtt_ms > 3_500:
+    if error_type in {"bad_gateway", "timeout", "connection_reset", "temporary_disconnect"} or last_rtt_ms > 3_000:
        return {"action": "switch_endpoint", "wait_ms": 0}
 
-    if attempt >= 3 or elapsed_ms > 15_000:
+    # Fail fast if total elapsed time is too high or max attempts reached
+    if elapsed_ms > 15_000 or attempt >= 3:
        return {"action": "fail", "wait_ms": 0}
 
+    # Switch endpoint if we hit congestion repeatedly
+    if attempt >= 1 and error_type in {"server_busy", "rate_limit"} and consecutive_failures >= 2:
+        return {"action": "switch_endpoint", "wait_ms": 0}
+
    if error_type == "rate_limit":
-        wait_ms = min(600 * (2 ** attempt), 8_000)
+        wait_ms = min(800 * (2 ** attempt), 8_000)
```

Explanation: This refinement pushed earlier switching at high RTT and added repeated-congestion switching. It improved latency further without changing success_rate.

### Step 4 - New Best at Iteration 9

- Transition: 39cfe3ca-9629-4338-823a-f0da63eeb97f -> 8e3390ac-14e3-4c36-9dda-1f18ffdd6b45
- Score: 9.0969 -> 10.8781 (delta +1.7812)
- Metrics before/after:
  - success_rate: 0.4688 -> 0.4688
  - avg_latency_ms: 627.5000 -> 533.7500
  - avg_retry_count: 2.0312 -> 2.0938
  - useless_retries: 1.6250 -> 1.6875
  - good_endpoint_switches: 0.1250 -> 0.1250

```diff
--- 39cfe3ca
+++ 8e3390ac
@@ -30,16 +30,15 @@
    if error_type in {"bad_gateway", "timeout", "connection_reset", "temporary_disconnect"} or last_rtt_ms > 3_000:
        return {"action": "switch_endpoint", "wait_ms": 0}
 
-    # Fail fast if total elapsed time is too high or max attempts reached
-    if elapsed_ms > 15_000 or attempt >= 3:
-        return {"action": "fail", "wait_ms": 0}
-
-    # Switch endpoint if we hit congestion repeatedly
+    # Switch endpoint if we hit repeated congestion
    if attempt >= 1 and error_type in {"server_busy", "rate_limit"} and consecutive_failures >= 2:
        return {"action": "switch_endpoint", "wait_ms": 0}
 
+    if attempt >= 3 or elapsed_ms > 15_000:
+        return {"action": "fail", "wait_ms": 0}
+
    if error_type == "rate_limit":
-        wait_ms = min(800 * (2 ** attempt), 8_000)
+        wait_ms = min(600 * (2 ** attempt), 8_000)
```

Explanation: The key change was backing off rate-limit waits, which delivered a sharp latency reduction and higher combined score, while keeping success_rate stable.

### Step 5 - New Best at Iteration 41

- Transition: 8e3390ac-14e3-4c36-9dda-1f18ffdd6b45 -> f77abb78-428e-46ac-9319-1fad1a862add
- Score: 10.8781 -> 12.2844 (delta +1.4062)
- Metrics before/after:
  - success_rate: 0.4688 -> 0.4688
  - avg_latency_ms: 533.7500 -> 486.8750
  - avg_retry_count: 2.0938 -> 2.0938
  - useless_retries: 1.6875 -> 1.6875
  - good_endpoint_switches: 0.1250 -> 0.1250

```diff
--- 8e3390ac
+++ f77abb78
@@ -26,19 +26,21 @@
    if consecutive_failures >= 5:
        return {"action": "open_circuit", "wait_ms": 5_000}
 
-    # Switch endpoint on critical network errors or high latency
+    # Switch endpoint on critical network errors or extreme latency
    if error_type in {"bad_gateway", "timeout", "connection_reset", "temporary_disconnect"} or last_rtt_ms > 3_000:
        return {"action": "switch_endpoint", "wait_ms": 0}
 
-    # Switch endpoint if we hit repeated congestion
-    if attempt >= 1 and error_type in {"server_busy", "rate_limit"} and consecutive_failures >= 2:
+    # Switch endpoint if we hit repeated congestion or persistent rate limits
+    if (attempt >= 1 and error_type in {"server_busy", "rate_limit"} and consecutive_failures >= 2) or \
+       (error_type == "rate_limit" and attempt >= 2):
        return {"action": "switch_endpoint", "wait_ms": 0}
 
-    if attempt >= 3 or elapsed_ms > 15_000:
+    # Fail fast if total elapsed time is too high or max attempts reached
+    if elapsed_ms > 13_000 or attempt >= 3:
        return {"action": "fail", "wait_ms": 0}
 
    if error_type == "rate_limit":
-        wait_ms = min(600 * (2 ** attempt), 8_000)
+        wait_ms = min(500 * (2 ** attempt), 7_000)
```

Explanation: The final jump came from tighter fail-fast timing and lower wait ceilings, especially for rate-limit. This reduced latency to 486.875 ms while preserving stability on other metrics.

## Plateau and Late Breakthrough Analysis

- From iterations 10 through 40, many candidates repeatedly landed at combined_score 10.8781, with nearly identical success_rate and switching behavior.
- This indicates a broad local optimum around the 8e3390ac policy shape.
- The run continued to explore neighboring variants, including lower-scoring branches (for example iterations 15, 19, 33, 35), but these did not improve global best.
- At iteration 41, a tighter parameterization (f77abb78) produced a latency improvement with unchanged success-rate envelope, unlocking the final best score.
- Iterations 42-50 then frequently rediscovered the same improved basin (scores of 12.2844 appearing repeatedly), confirming the new optimum was stable and reproducible.

## Checkpoint Hash Trend for best_program.py

- Checkpoint 5: 62b7827092e936ff9fb37f97ae2ec19e
- Checkpoints 10-40: f915f3bd1f2a313a78a1aa20203c042d
- Checkpoints 45-50 and current best: 4e2f4f6d246b5d178fb390594590e708

Interpretation: the run had two major policy-shape phases after the early stage, with the second phase beginning between checkpoints 40 and 45 and matching the final best artifact.

## Final Best Summary

- Best program id: f77abb78-428e-46ac-9319-1fad1a862add
- First found at: iteration 41
- Final combined_score: 12.2844
- success_rate: 0.4688
- avg_latency_ms: 486.8750
- avg_retry_count: 2.0938
- useless_retries: 1.6875
- good_endpoint_switches: 0.1250

This run shows a classic pattern: rapid early gains, long plateau with repeated rediscovery of a strong local optimum, then a late parameter-tuning breakthrough that mainly improved latency while preserving safety and success behavior.
