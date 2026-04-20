"""Synthetic scenarios for retry/backoff evolution.

The goal is not perfect realism. The goal is structured, fast, deterministic
feedback that is difficult to game accidentally.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List
import random


ERRORS = [
    "timeout",
    "connection_reset",
    "server_busy",
    "rate_limit",
    "bad_gateway",
    "temporary_disconnect",
    "slow_response",
    "invalid_request",  # non-retryable
]


@dataclass(frozen=True)
class Scenario:
    name: str
    error_type: str
    is_idempotent: bool
    max_attempts: int
    recovery_attempt: int | None
    recovery_after_elapsed_ms: int | None
    primary_endpoint_bad_until_attempt: int | None
    latency_ms: int
    duplicate_risk: float
    description: str


def _core_train_scenarios() -> List[Scenario]:
    return [
        Scenario(
            name="timeout_then_success_3",
            error_type="timeout",
            is_idempotent=True,
            max_attempts=5,
            recovery_attempt=3,
            recovery_after_elapsed_ms=None,
            primary_endpoint_bad_until_attempt=None,
            latency_ms=120,
            duplicate_risk=0.0,
            description="Transient timeout clears on third attempt.",
        ),
        Scenario(
            name="rate_limit_needs_cooldown",
            error_type="rate_limit",
            is_idempotent=True,
            max_attempts=4,
            recovery_attempt=None,
            recovery_after_elapsed_ms=900,
            primary_endpoint_bad_until_attempt=None,
            latency_ms=80,
            duplicate_risk=0.0,
            description="429-style scenario requiring enough wait time.",
        ),
        Scenario(
            name="server_busy_then_recovers",
            error_type="server_busy",
            is_idempotent=True,
            max_attempts=5,
            recovery_attempt=None,
            recovery_after_elapsed_ms=1300,
            primary_endpoint_bad_until_attempt=None,
            latency_ms=100,
            duplicate_risk=0.0,
            description="Overloaded service recovers after elapsed threshold.",
        ),
        Scenario(
            name="connection_reset_fast_recovery",
            error_type="connection_reset",
            is_idempotent=True,
            max_attempts=4,
            recovery_attempt=2,
            recovery_after_elapsed_ms=None,
            primary_endpoint_bad_until_attempt=None,
            latency_ms=40,
            duplicate_risk=0.0,
            description="Transport glitch usually recovers quickly.",
        ),
        Scenario(
            name="primary_endpoint_bad_switch_helps",
            error_type="bad_gateway",
            is_idempotent=True,
            max_attempts=4,
            recovery_attempt=None,
            recovery_after_elapsed_ms=None,
            primary_endpoint_bad_until_attempt=99,
            latency_ms=70,
            duplicate_risk=0.0,
            description="Primary endpoint remains degraded; switch should help.",
        ),
        Scenario(
            name="non_idempotent_timeout_danger",
            error_type="timeout",
            is_idempotent=False,
            max_attempts=3,
            recovery_attempt=2,
            recovery_after_elapsed_ms=None,
            primary_endpoint_bad_until_attempt=None,
            latency_ms=150,
            duplicate_risk=1.0,
            description="Retry may duplicate side effects; fail-fast is safer.",
        ),
        Scenario(
            name="permanent_disconnect",
            error_type="temporary_disconnect",
            is_idempotent=True,
            max_attempts=5,
            recovery_attempt=None,
            recovery_after_elapsed_ms=None,
            primary_endpoint_bad_until_attempt=None,
            latency_ms=50,
            duplicate_risk=0.0,
            description="Never recovers within useful budget.",
        ),
        Scenario(
            name="invalid_request_non_retryable",
            error_type="invalid_request",
            is_idempotent=True,
            max_attempts=2,
            recovery_attempt=None,
            recovery_after_elapsed_ms=None,
            primary_endpoint_bad_until_attempt=None,
            latency_ms=10,
            duplicate_risk=0.0,
            description="Business/protocol error; should fail immediately.",
        ),
    ]


def _holdout_scenarios() -> List[Scenario]:
    return [
        Scenario(
            name="slow_response_then_success",
            error_type="slow_response",
            is_idempotent=True,
            max_attempts=5,
            recovery_attempt=3,
            recovery_after_elapsed_ms=None,
            primary_endpoint_bad_until_attempt=None,
            latency_ms=2500,
            duplicate_risk=0.0,
            description="Large RTT should influence patience and delay.",
        ),
        Scenario(
            name="rate_limit_longer_cooldown",
            error_type="rate_limit",
            is_idempotent=True,
            max_attempts=5,
            recovery_attempt=None,
            recovery_after_elapsed_ms=1800,
            primary_endpoint_bad_until_attempt=None,
            latency_ms=90,
            duplicate_risk=0.0,
            description="Holdout variant with longer cooldown than training.",
        ),
        Scenario(
            name="non_idempotent_bad_gateway",
            error_type="bad_gateway",
            is_idempotent=False,
            max_attempts=3,
            recovery_attempt=None,
            recovery_after_elapsed_ms=None,
            primary_endpoint_bad_until_attempt=99,
            latency_ms=60,
            duplicate_risk=0.8,
            description="Switch may be better than retry for dangerous writes.",
        ),
        Scenario(
            name="server_busy_short_recovery",
            error_type="server_busy",
            is_idempotent=True,
            max_attempts=4,
            recovery_attempt=None,
            recovery_after_elapsed_ms=600,
            primary_endpoint_bad_until_attempt=None,
            latency_ms=120,
            duplicate_risk=0.0,
            description="Faster holdout recovery than train scenario.",
        ),
    ]


def _randomized(seed: int, n: int) -> List[Scenario]:
    rnd = random.Random(seed)
    scenarios: List[Scenario] = []
    for idx in range(n):
        error_type = rnd.choice(ERRORS[:-1])
        is_idempotent = rnd.random() < 0.75
        latency = rnd.choice([40, 60, 80, 120, 200, 400, 1000, 2500])
        mode = rnd.choice(["attempt", "elapsed", "never", "switch"])
        recovery_attempt = None
        recovery_after_elapsed_ms = None
        primary_endpoint_bad_until_attempt = None
        if mode == "attempt":
            recovery_attempt = rnd.randint(2, 4)
        elif mode == "elapsed":
            recovery_after_elapsed_ms = rnd.choice([500, 900, 1300, 1800])
        elif mode == "switch":
            primary_endpoint_bad_until_attempt = 99
        duplicate_risk = 0.0 if is_idempotent else rnd.choice([0.5, 0.8, 1.0])
        scenarios.append(
            Scenario(
                name=f"rnd_{seed}_{idx}_{error_type}_{mode}",
                error_type=error_type,
                is_idempotent=is_idempotent,
                max_attempts=rnd.randint(3, 5),
                recovery_attempt=recovery_attempt,
                recovery_after_elapsed_ms=recovery_after_elapsed_ms,
                primary_endpoint_bad_until_attempt=primary_endpoint_bad_until_attempt,
                latency_ms=latency,
                duplicate_risk=duplicate_risk,
                description="Seeded randomized scenario.",
            )
        )
    return scenarios


def build_train_scenarios(seed: int = 42) -> List[Scenario]:
    return _core_train_scenarios() + _randomized(seed=seed, n=24)


def build_holdout_scenarios(seed: int = 314) -> List[Scenario]:
    return _holdout_scenarios() + _randomized(seed=seed, n=12)
