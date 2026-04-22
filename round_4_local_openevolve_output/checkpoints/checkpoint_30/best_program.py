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
    if circuit_open:
        return {"action": "fail", "wait_ms": 0}

    if error_type not in RETRYABLE_ERRORS:
        return {"action": "fail", "wait_ms": 0}

    if not is_idempotent and attempt > 0:
        return {"action": "fail", "wait_ms": 0}

    if consecutive_failures >= 5:
        return {"action": "open_circuit", "wait_ms": 5_000}

    if attempt >= 3:
        return {"action": "fail", "wait_ms": 0}

    if error_type == "rate_limit":
        wait_ms = min(500 * (2 ** attempt), 8_000)
    elif error_type == "server_busy":
        wait_ms = min(250 * (2 ** attempt), 4_000)
    else:
        wait_ms = min(100 * (2 ** attempt), 2_000)

    if last_rtt_ms > 2_000:
        wait_ms += 250

    return {"action": "retry", "wait_ms": wait_ms}
# EVOLVE-BLOCK-END
