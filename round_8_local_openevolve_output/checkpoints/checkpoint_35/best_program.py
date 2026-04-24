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
    """Return the next retry-control action.

    Contract:
    - action in {retry, fail, switch_endpoint, open_circuit}
    - wait_ms is a non-negative integer
    """
    # Circuit breaker logic first - critical for preventing infinite loops
    if circuit_open:
        return {"action": "fail", "wait_ms": 0}

    # Non-retryable errors always fail immediately
    if error_type not in RETRYABLE_ERRORS:
        return {"action": "fail", "wait_ms": 0}

    # Non-idempotent operations: fail after first attempt
    if not is_idempotent and attempt > 0:
        return {"action": "fail", "wait_ms": 0}

    # Overall time limit check - prevent runaway operations
    if elapsed_ms > 10_000:
        return {"action": "fail", "wait_ms": 0}

    # Consecutive failures threshold - open circuit before hard limit
    if consecutive_failures >= 5:
        return {"action": "open_circuit", "wait_ms": 5_000}

    # Total attempts limit - prevent infinite loops
    if attempt >= 3:
        return {"action": "fail", "wait_ms": 0}

    # Calculate base wait time with error-type specific strategies
    if error_type == "rate_limit":
        # More aggressive rate limiting - shorter waits
        wait_ms = min(400 * (2 ** attempt), 6_000)
    elif error_type == "server_busy":
        # Moderate wait for server_busy errors
        wait_ms = min(200 * (2 ** attempt), 3_500)
    elif error_type in {"timeout", "connection_reset"}:
        # Slightly shorter waits for network-related errors
        wait_ms = min(80 * (2 ** attempt), 1_800)
    else:
        # Default for other error types
        wait_ms = min(70 * (2 ** attempt), 1_600)

    # RTT-based adjustment - only add delay for very high latency
    if last_rtt_ms > 2_500:
        wait_ms = min(wait_ms + 150, 6_150)
    elif last_rtt_ms > 1_500:
        # Small adjustment for moderate latency
        wait_ms = min(wait_ms + 50, 1_650)

    return {"action": "retry", "wait_ms": wait_ms}
# EVOLVE-BLOCK-END