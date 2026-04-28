# Lessons Learned

Distilled observations from running OpenEvolve against this retry-policy
problem with hosted and local models. Each lesson is meant to be useful
beyond this specific repository.

## 1. The evaluator is the real product

The evolved policy is the visible artifact, but most of the engineering
value is in the evaluator: scenarios, metric weights, safety penalties,
and the train/holdout split. Improving the evaluator improves every
future run; improving a single candidate does not.

If you only have time to harden one thing in an evaluation-first AI
system, harden the evaluator.

## 2. LLM-generated improvement can be misleading

A candidate that improves `combined_score` is not automatically better.
Multiple observed candidates increased train score primarily by failing
faster, which reduced latency but also reduced success rate. Without a
breakdown view, this would have looked like a win.

Treat scalar score as a *trigger for review*, not as a pass/fail signal.

## 3. Holdout validation is mandatory

The same candidate that improves train metrics can regress holdout
reliability. The classic example here: train `combined_score` went up
while holdout `success_rate` went down. A train-only acceptance loop
would have shipped the regression.

Holdout is cheap; skipping it is expensive.

## 4. Local models fail differently from hosted models

Hosted models tend to fail by being *over-confident* and producing
plausible but subtly wrong code. Small local models tend to fail by:

- producing prose instead of code
- not changing anything (no-op diff)
- changing the function signature
- inventing keys (`wait_time` instead of `wait_ms`)
- referencing undefined variables

These are different categories of failure and require different defenses
(stricter contract tests, normalization, prompt constraints).

## 5. Small models can still be useful when the mutation surface is narrow

`qwen2.5-coder:1.5b` and `qwen2.5-coder:3b` produced valid, contract-
respecting diffs in this repo. Local small models become viable when:

- the editable region is one small function
- the contract is enforced by tests and a normalizer
- the evaluator filters bad candidates fast

This makes "local LLM + tight evaluator" a workable pattern for cheap,
private, fast iteration loops.

## 6. Combined score is not enough

The single-number objective is convenient for search but dangerous for
acceptance. Always look at:

- success rate
- safety counters (`dangerous_non_idempotent_retries`)
- latency
- retry counts
- behavioral counters (`good_fail_fast_decisions`, `good_endpoint_switches`)

Acceptance must be constraint-first, not score-first.

## 7. Reward hacking appears quickly

With a small mutation surface and a scalar objective, reward hacking
showed up within a handful of iterations. The most common pattern was
"fail fast on more error types" — score went up, behavior got worse.

Anticipate reward hacking by encoding the hacks themselves as penalties.

## 8. QA knowledge matters

Designing the evaluator is QA / SDET work, not ML work. The questions
are the same as in any test design exercise:

- what failure modes do I care about?
- what invariants must hold?
- what does "better" mean in operational terms?
- how do I detect a regression that improves a proxy metric?

LLMs accelerate code generation. They do not replace test design.

## 9. This pattern generalizes

The pattern — narrow mutation surface, deterministic evaluator, train /
holdout split, hard safety gates — applies far beyond retry policy:

- fintech protocol handlers (FIX, ITCH, OUCH lifecycle edge cases)
- post-trade reconciliation rules
- document-processing QA pipelines
- LLM output regression testing
- workflow validators in complex backends

The retry policy is a small proof of the pattern, not the pattern itself.

## 10. The weakest link is simulator realism

The model is rarely the bottleneck. The bottleneck is whether the
simulated world the candidate is being evaluated against resembles the
real one. Investing in better scenarios, more realistic failure
distributions, and adversarial holdouts pays off more than swapping models.

If the simulator is wrong, every candidate optimizes for a world that
does not exist.
