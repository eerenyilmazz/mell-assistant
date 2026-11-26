# 0008. Authenticated localhost backend and loopback-only services

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

Scans in 2025–2026 found from about a thousand to about 175,000 Ollama servers reachable from the internet, usually after one bind-address change. A popular self-hosted assistant was also hijacked by malicious web pages calling its unauthenticated local endpoint (PLAN.md 3.1).

## Decision

Ollama and PostgreSQL bind to `127.0.0.1` only. The backend binds to loopback, and to the private-network interface only when cross-device access is enabled. The backend requires authentication even on localhost, validates `Origin` and `Host`, and has no unauthenticated WebSocket or SSE endpoint. A startup self-check refuses to run if any service is bound to a public interface.

## Options

- Trust localhost (no auth on loopback) — any web page in the user's browser can drive the agent.
- Expose services on the LAN for convenience — the common path to public exposure.
- Rely on the OS firewall only — one misconfiguration away from exposure; not testable in the app.
- Do nothing — default bindings vary by tool and version.

## Consequences

- **+** Local web pages and LAN devices cannot reach the model runtime, database or agent.
- **+** Exposure is detected by the app itself at startup.
- **−** Local development needs a login and CSRF handling from Phase 0.

## Risk

Low. Mitigation: integration test for unauthenticated and cross-origin requests (PLAN.md 14.1).

## Rollback

Bindings are configuration; relaxing them requires a superseding ADR because it removes a security control.
