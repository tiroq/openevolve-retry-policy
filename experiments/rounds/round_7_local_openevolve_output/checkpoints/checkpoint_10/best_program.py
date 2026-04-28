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

    This version optimizes for higher success rates by expanding the 
    endpoint-switching criteria and refining the backoff timing to be 
    more aggressive on transient errors while patient with rate limits.
    """
    if circuit_open:
        return {"action": "fail", "wait_ms": 0}

    if error_type not in RETRYABLE_ERRORS:
        return {"action": "fail", "wait_ms": 0}

    # Safety: No retries for non-idempotent requests after the first failure
    if not is_idempotent and attempt > 0:
        return {"action": "fail", "wait_ms": 0}

    # Circuit breaker for high failure streaks
    if consecutive_failures >= 4:
        return {"action": "open_circuit", "wait_ms": 5_000}

    # Fail fast to avoid excessive latency
    if attempt >= 3:
        return {"action": "fail", "wait_ms": 0}

    # Strategic Endpoint Switching:
    # Switch on network-level errors to bypass localized infrastructure issues.
    # Include 'temporary_disconnect' and 'slow_response' as triggers.
    switch_triggers = {"bad_gateway", "connection_reset", "timeout", "temporary_disconnect", "slow_response"}
    if error_type in switch_triggers and attempt >= 1:
        return {"action": "switch_endpoint", "wait_ms": 150}

    # Differentiated Backoff
    if error_type == "rate_limit":
        # Rate limits require longer, more stable pauses
        wait_ms = 1200 * (2 ** attempt)
    elif error_type == "server_busy":
        # Server load is usually transient
        wait_ms = 600 * (2 ** attempt)
    else:
        # General network errors use a tighter backoff for lower latency
        wait_ms = 200 * (2 ** attempt)

    # Dynamic latency adjustment: 
    # If RTT is high, we add a penalty to avoid congesting the pipe
    if last_rtt_ms > 1200:
        wait_ms += 300

    return {"action": "retry", "wait_ms": min(wait_ms, 10_000)}
# EVOLVE-BLOCK-END