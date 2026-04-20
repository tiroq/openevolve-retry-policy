from initial_program import VALID_ACTIONS, choose_action, normalize_action


def test_choose_action_returns_valid_shape():
    raw = choose_action(0, "timeout", 0, 100, 0, True, False)
    normalized = normalize_action(raw)
    assert normalized["action"] in VALID_ACTIONS
    assert isinstance(normalized["wait_ms"], int)
    assert normalized["wait_ms"] >= 0


def test_non_retryable_fails_fast():
    raw = choose_action(0, "invalid_request", 0, 50, 0, True, False)
    normalized = normalize_action(raw)
    assert normalized["action"] == "fail"


def test_non_idempotent_retry_is_not_allowed_after_first_attempt():
    raw = choose_action(1, "timeout", 100, 80, 1, False, False)
    normalized = normalize_action(raw)
    assert normalized["action"] in {"fail", "open_circuit"}
