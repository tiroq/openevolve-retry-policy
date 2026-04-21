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

    if consecutive_failures >= 2 and error_type in {"bad_gateway", "timeout"}:
        return {"action": "switch_endpoint", "wait_ms": 0}

    if attempt >= 3:
        return {"action": "fail", "wait_ms": 0}

    if last_rtt_ms > 5_000:
        return {"action": "switch_endpoint", "wait_ms": 0}

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
