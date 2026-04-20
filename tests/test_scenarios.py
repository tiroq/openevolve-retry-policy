from scenarios import build_holdout_scenarios, build_train_scenarios


def test_train_scenarios_are_deterministic():
    a = build_train_scenarios(seed=42)
    b = build_train_scenarios(seed=42)
    assert a == b


def test_holdout_scenarios_are_deterministic():
    a = build_holdout_scenarios(seed=314)
    b = build_holdout_scenarios(seed=314)
    assert a == b


def test_holdout_scenarios_are_non_empty():
    scenarios = build_holdout_scenarios()
    assert len(scenarios) >= 4


def test_train_and_holdout_are_not_identical():
    train_names = {s.name for s in build_train_scenarios()}
    holdout_names = {s.name for s in build_holdout_scenarios()}
    assert train_names != holdout_names


def test_train_scenario_count():
    assert len(build_train_scenarios()) == 32


def test_holdout_scenario_count():
    assert len(build_holdout_scenarios()) == 16
