"""Initial retry policy for OpenEvolve.

OpenEvolve should mutate only the EVOLVE-BLOCK below.
Everything outside the block is treated as stable helper code.
"""

from __future__ import annotations

from typing import Dict


RETRYABLE_ERRORS = {
    "timeout",
    "connection_reset",
    "server_busy",
    "rate_limit",
    "bad_gateway",
    "temporary_disconnect",
    "slow_response",
}

VALID_ACTIONS = {"retry", "fail", "switch_endpoint", "open_circuit"}


def normalize_action(payload: Dict[str, int | str]) -> Dict[str, int | str]:
    """Defensive normalization used by the evaluator.

    The evolve block should still try to return correct values directly.
    """
    action = payload.get("action", "fail")
    if action not in VALID_ACTIONS:
        action = "fail"

    wait_ms = payload.get("wait_ms", 0)
    if not isinstance(wait_ms, int):
        try:
            wait_ms = int(wait_ms)
        except Exception:
            wait_ms = 0
    wait_ms = max(0, min(wait_ms, 30_000))
    return {"action": action, "wait_ms": wait_ms}


# EVOLVE-BLOCK-START
def choose_action(
    attempt: int,
    error_type: str,
    elapsed_ms: int,
    last_rtt_ms: int,
    consecutive_failures: int,
    is_idempotent: bool,
    circuit_open: bool,
) -> Dict[str, int | str]:
    """
    Optimized retry policy to maximize fitness.
    
    Improvements:
    1. Aggressive Fail-Fast: Limit attempts strictly to 2 (0, 1) to minimize useless_retries.
    2. High-Precision Switching: Switch endpoints immediately on attempt 1 for network errors.
    3. Idempotency Guard: Absolute zero tolerance for non-idempotent retries.
    4. Rapid Circuit Breaking: Open circuit on 3 consecutive failures.
    5. Refined Backoff: Tightened wait times to reduce latency while maintaining success.
    """
    # Immediate fail for circuit open or non-retryable errors
    if circuit_open or error_type not in RETRYABLE_ERRORS:
        return {"action": "fail", "wait_ms": 0}

    # Safety: Non-idempotent requests must never be retried
    if not is_idempotent and attempt > 0:
        return {"action": "fail", "wait_ms": 0}

    # Circuit breaker: Trigger rapidly on failure streaks
    if consecutive_failures >= 3:
        return {"action": "open_circuit", "wait_ms": 3000}

    # Fail fast: Cap at 2 attempts (0 and 1) to optimize latency and useless_retries
    if attempt >= 2:
        return {"action": "fail", "wait_ms": 0}

    # Strategic Endpoint Switching:
    # Switch on the first retry (attempt 1) for infrastructure-level failures to bypass bad nodes.
    switch_triggers = {"bad_gateway", "connection_reset", "timeout", "temporary_disconnect", "slow_response"}
    if attempt >= 1 and error_type in switch_triggers:
        return {"action": "switch_endpoint", "wait_ms": 100}

    # Tiered Backoff based on error type
    if error_type == "rate_limit":
        # Rate limits need a significant window to reset
        wait_ms = 1400 * (2 ** attempt)
    elif error_type == "server_busy":
        # Server load is transient
        wait_ms = 700 * (2 ** attempt)
    else:
        # Fast recovery for transient network glitches
        wait_ms = 250 * (2 ** attempt)

    # Congestion avoidance: Add delay if network RTT is high
    if last_rtt_ms > 1000:
        wait_ms += 150

    return {"action": "retry", "wait_ms": min(wait_ms, 10_000)}
# EVOLVE-BLOCK-END