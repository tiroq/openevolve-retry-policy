# Positioning

> **Building evaluation-first AI systems for QA automation, reliability
> testing, and complex workflow validation.**

This repository is a compact, public proof-of-work demonstrating that
positioning. It is intentionally small — one function, one evaluator,
one mutation block — so that the *discipline* around AI-assisted code
change is visible without being buried in domain code.

## Why a retry policy is a good small proxy

Retry/backoff sits at the intersection of three things that matter for
serious backend work:

- **Reliability under partial failure.** The policy decides how the
  system behaves when the world is unstable. Wrong choices cause
  outages, duplicated side effects, or wasted budget.
- **Idempotency awareness.** Retrying a non-idempotent request after
  the first attempt is a real production hazard. The evaluator
  encodes this as a hard penalty.
- **Narrow but realistic search space.** Small enough for local LLMs
  and short feedback loops; large enough to admit reward hacking,
  overfitting, and contract drift.

That makes it a good *miniature* of larger evaluation-first AI work.

## How this maps to QA automation

The work in this repo is recognizable QA automation:

- deterministic test scenarios with stable seeds
- explicit invariants and acceptance gates
- separation of "search data" (train) and "validation data" (holdout)
- catalog of observed failure modes
- per-run report template

The novelty is the *subject under test*: not human-written code, but
LLM-generated code mutations. The QA mindset transfers cleanly.

## How this maps to reliability engineering

Retry/backoff, circuit breaking, and endpoint failover are core
reliability primitives. The evaluator scores candidates on:

- success rate under transient failure
- safe handling of non-idempotent operations
- latency under load
- correct fail-fast behavior
- correct use of endpoint switches

These are the same primitives that decide whether a real distributed
system stays available during incidents.

## How this maps to complex workflow validation

Many real systems — order routing, post-trade processing, document
ingestion pipelines, multi-step LLM agents — are essentially long
sequences of "what should I do next given this state?" decisions.
That is exactly the shape of `choose_action()`.

The evaluator pattern in this repo (deterministic state, behavioral
counters, hard safety gates, holdout split) is reusable for any of
these workflows.

## Future directions

The same evaluation-first pattern can be applied to:

- **Fintech protocol testing** — FIX / ITCH / OUCH session and order
  lifecycle edge cases, replayed deterministically.
- **FIX message lifecycle validation** — sequence numbers, resends,
  gap fills, logon/logout invariants.
- **Post-trade reconciliation** — rule-based matching with strict
  acceptance criteria and a holdout day of trades.
- **Document-processing QA** — mdify-style pipelines with golden
  outputs, regression detection, and adversarial inputs.
- **LLM output regression testing** — deterministic harnesses that
  check structure, schema, and behavioral invariants of generated
  outputs over time.
- **AI-assisted test generation** — using LLMs to propose new
  scenarios, then gating them through the same kind of evaluator
  this repo demonstrates.

Each of these is a larger project than retry policy. The point of
this repository is to show that the *evaluation discipline* is the
transferable asset — not the specific domain.
