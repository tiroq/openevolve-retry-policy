# Evolution Report Template

## Summary

- Run date:
- Model setup:
- Iterations:
- Dataset split:
- Best train `combined_score`:
- Best holdout `combined_score`:

## Baseline vs Evolved

| Metric | Baseline Train | Evolved Train | Baseline Holdout | Evolved Holdout |
| --- | ---: | ---: | ---: | ---: |
| success_rate |  |  |  |  |
| avg_latency_ms |  |  |  |  |
| avg_retry_count |  |  |  |  |
| dangerous_non_idempotent_retries |  |  |  |  |
| useless_retries |  |  |  |  |
| good_fail_fast_decisions |  |  |  |  |
| good_endpoint_switches |  |  |  |  |
| combined_score |  |  |  |  |

## Best observed behavior changes

- 
- 
- 

## Regressions or suspicious behavior

- 
- 
- 

## Generalization assessment

- Did holdout improve?
- Is the gain mostly due to aggressive retries, fail-fast behavior, or switching?
- Does the result look robust or reward-hacked?

## Weakest link

- The weakest link in this run was:
- Why it matters:
- What to change next:
