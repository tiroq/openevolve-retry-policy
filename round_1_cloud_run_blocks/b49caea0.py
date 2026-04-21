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

    # Switch endpoint on critical network errors or high latency
    if error_type in {"bad_gateway", "timeout", "connection_reset", "temporary_disconnect"} or last_rtt_ms > 3_500:
        return {"action": "switch_endpoint", "wait_ms": 0}

    if attempt >= 3 or elapsed_ms > 15_000:
        return {"action": "fail", "wait_ms": 0}

    if error_type == "rate_limit":
        wait_ms = min(600 * (2 ** attempt), 8_000)
    elif error_type == "server_busy":
        wait_ms = min(400 * (2 ** attempt), 4_000)
    else:
        wait_ms = min(200 * (2 ** attempt), 2_500)

    # Add jitter/extra wait if RTT is creeping up
    if last_rtt_ms > 2_000:
        wait_ms += 300

    return {"action": "retry", "wait_ms": wait_ms}
# EVOLVE-BLOCK-END
