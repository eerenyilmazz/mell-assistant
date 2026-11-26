# 0006. Manual model selection before automatic routing

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

The first draft routed each request automatically between a general, a coding and a cloud model. On a 12 GB GPU, switching between several 7–8B models causes cold loads that dominate latency, and there is no evaluation data yet to justify routing rules (PLAN.md 7.3, 7.5).

## Decision

In v0.1 the user selects the model per conversation. One local chat model and one embedding model stay resident. Rule-based routing is introduced in Phase 4 only after the evaluation set shows where each model wins; every routing decision will be logged.

## Options

- Automatic LLM-based routing from day one — extra latency and an untested classifier making invisible choices.
- Rule-based routing from day one — rules would be guesses without measurements.
- Cloud-only — simplest, but conflicts with local-first and sensitive-data rules.
- Do nothing (single fixed model) — no way to compare or fall back.

## Consequences

- **+** Predictable behaviour and latency; no model swapping on the GPU.
- **+** Usage logs per model build the data for later routing.
- **−** The user must choose a model; no automatic escalation to a stronger model.

## Risk

Low. Mitigation: clear model selector in the UI; defaults set from the Phase 1 baseline.

## Rollback

Routing is added inside the `ai` module behind the same port; manual selection remains as an override.
