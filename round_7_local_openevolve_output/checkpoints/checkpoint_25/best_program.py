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

    Refined to maximize fitness by aggressively pruning useless retries
    and optimizing endpoint switching for network-level failures.
    """
    if circuit_open:
        return {"action": "fail", "wait_ms": 0}

    if error_type not in RETRYABLE_ERRORS:
        return {"action": "fail", "wait_ms": 0}

    # Safety: Never retry non-idempotent requests
    if not is_idempotent and attempt > 0:
        return {"action": "fail", "wait_ms": 0}

    # Circuit breaker: Trigger on a moderate streak to prevent cascading failure
    if consecutive_failures >= 3:
        return {"action": "open_circuit", "wait_ms": 3000}

    # Fail fast: Limit to 2 attempts total to minimize 'useless_retries' and latency
    if attempt >= 2:
        return {"action": "fail", "wait_ms": 0}

    # Strategic Endpoint Switching:
    # Switch on the first retry (attempt 1) for infrastructure-level errors.
    # This bypasses bad nodes quickly.
    switch_triggers = {"bad_gateway", "connection_reset", "timeout", "temporary_disconnect", "slow_response"}
    if attempt >= 1 and error_type in switch_triggers:
        return {"action": "switch_endpoint", "wait_ms": 100}

    # Tiered Exponential Backoff
    if error_type == "rate_limit":
        # Rate limits need substantial time to reset
        wait_ms = 1500 * (2 ** attempt)
    elif error_type == "server_busy":
        # Server load is transient but needs a small gap
        wait_ms = 800 * (2 ** attempt)
    else:
        # Fast recovery for transient network glitches
        wait_ms = 300 * (2 ** attempt)

    # Congestion avoidance: Add delay if the network is showing high latency
    if last_rtt_ms > 1000:
        wait_ms += 200

    return {"action": "retry", "wait_ms": min(wait_ms, 10_000)}
# EVOLVE-BLOCK-END