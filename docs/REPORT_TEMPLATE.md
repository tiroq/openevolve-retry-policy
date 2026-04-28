# Run Report Template

Use this template for every OpenEvolve run that is worth documenting.
Keep it short, factual, and honest. The goal is reproducibility and
auditability, not narrative.

## Run metadata

- Run date:
- Run ID / output dir:
- Iterations:
- Wall-clock time:
- Author / operator:

## Model config

- Primary model:
- Secondary model:
- Temperature / sampling settings:
- Local / hosted:
- Inference backend (Ollama / vLLM / LM Studio / OpenRouter / other):

## Endpoint config

- `api_base`:
- Auth model (if any):
- Notes on rate limits / latency:

## Prompt / template notes

- System prompt source:
- Any custom evaluator system message
  ([templates/evaluator_system_message.txt](../templates/evaluator_system_message.txt)):
- Mutation instructions / constraints:

## Baseline metrics

Train:

```json
{
  "avg_latency_ms": ,
  "avg_retry_count": ,
  "combined_score": ,
  "dangerous_non_idempotent_retries": ,
  "good_endpoint_switches": ,
  "good_fail_fast_decisions": ,
  "runs_successfully": ,
  "success_rate": ,
  "useless_retries":
}
```

Holdout:

```json
{
  "avg_latency_ms": ,
  "avg_retry_count": ,
  "combined_score": ,
  "dangerous_non_idempotent_retries": ,
  "good_endpoint_switches": ,
  "good_fail_fast_decisions": ,
  "runs_successfully": ,
  "success_rate": ,
  "useless_retries":
}
```

## Candidate metrics

Train:

```json
{
}
```

Holdout:

```json
{
}
```

## Train metrics — comparison

| Metric | Baseline | Candidate | Delta |
| --- | ---: | ---: | ---: |
| success_rate |  |  |  |
| avg_latency_ms |  |  |  |
| avg_retry_count |  |  |  |
| dangerous_non_idempotent_retries |  |  |  |
| useless_retries |  |  |  |
| good_fail_fast_decisions |  |  |  |
| good_endpoint_switches |  |  |  |
| combined_score |  |  |  |

## Holdout metrics — comparison

| Metric | Baseline | Candidate | Delta |
| --- | ---: | ---: | ---: |
| success_rate |  |  |  |
| avg_latency_ms |  |  |  |
| avg_retry_count |  |  |  |
| dangerous_non_idempotent_retries |  |  |  |
| useless_retries |  |  |  |
| good_fail_fast_decisions |  |  |  |
| good_endpoint_switches |  |  |  |
| combined_score |  |  |  |

## Diff summary

- Lines changed (in EVOLVE-BLOCK):
- Lines changed (outside EVOLVE-BLOCK — should be 0):
- Behavioral nature of the diff (e.g. "expanded retry to cover slow_response"):

## Safety review

- [ ] No dangerous non-idempotent retries
- [ ] No undefined variables
- [ ] No new imports
- [ ] No external state
- [ ] Function signature preserved
- [ ] Return shape preserved

## Failure modes observed

Reference [docs/MODEL_FAILURE_MODES.md](../docs/MODEL_FAILURE_MODES.md).

- 

## Verdict

- [ ] Accepted
- [ ] Rejected
- [ ] Inconclusive / promising — requires more validation

## Reasoning

Brief, honest justification of the verdict, written *after* reviewing
the diff and the metric breakdown — not just the combined score.

## Follow-up experiments

- 
- 
- 
