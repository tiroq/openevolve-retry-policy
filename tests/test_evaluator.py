from evaluator import evaluate_program


def test_evaluator_returns_combined_score():
    result = evaluate_program("initial_program.py", dataset="train")
    assert "combined_score" in result.metrics
    assert result.metrics["runs_successfully"] == 1.0


def test_holdout_evaluation_runs():
    result = evaluate_program("initial_program.py", dataset="holdout")
    assert result.metrics["runs_successfully"] == 1.0
    assert result.metrics["avg_latency_ms"] >= 0
