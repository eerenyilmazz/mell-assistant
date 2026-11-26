# 0007. Defer Redis, Tauri, voice and external actions beyond v0.1

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

The project is built by one part-time developer alongside other work. The largest risk is scope growth stalling the project before a usable core exists (PLAN.md 5, R-1). Comparable projects show voice and broad tool access are where effort and risk concentrate.

## Decision

v0.1 (Phases 0–2) contains only: local streaming chat, conversation history, explicit memory with a Memory Center, manual model selection, read-only device tools behind the Permission Engine, and the activity log. Redis, Tauri packaging, voice, multi-agent orchestration and any external-communication or destructive tool are deferred to later phases with their own exit criteria.

## Options

- Build all modules in parallel — high risk of an unfinished system.
- Start with voice — most visible, but most expensive and depends on the core.
- Start with desktop packaging — packaging an app that does not yet work.
- Do nothing — no plan for scope control.

## Consequences

- **+** A usable, testable core early; later phases build on measured behaviour.
- **+** Security model proven on read-only tools before write or external tools exist.
- **−** v0.1 runs in a browser on localhost, not as a desktop app.
- **−** No voice until Phase 5.

## Risk

Low. Mitigation: Phase 2 gate (PLAN.md 14.4) must pass before Phases 3–8 start.

## Rollback

Any deferred item can be pulled forward by a superseding ADR stating what moves out to make room.
