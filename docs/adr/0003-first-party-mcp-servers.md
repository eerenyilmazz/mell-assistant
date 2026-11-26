# 0003. First-party MCP servers for tool and device integration

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

MELL must act on two machines (Windows host, Mac). The first draft planned a custom device-agent protocol. MCP is a standard tool protocol with Tier 1 SDKs, but research shows tool poisoning and malicious third-party servers are the most common MCP risks (PLAN.md 3.1).

## Decision

Expose device capabilities through MCP servers written in this repository. Only first-party servers are allowed in v0.x. Each tool definition is shown to the user, approved, pinned by hash, and disabled if its hash changes.

## Options

- Custom command protocol — no ecosystem, more code to secure, nothing reusable.
- MCP with third-party servers allowed — fastest feature growth; largest attack surface (malicious or modified servers).
- Direct OS calls from the backend — couples the backend to each OS and breaks cross-device routing.
- Do nothing — no device actions.

## Consequences

- **+** Standard protocol, official TypeScript SDK, reusable tooling (inspector, tests).
- **+** Rug-pull and tool-poisoning risks reduced by first-party code and definition pinning.
- **−** Every tool must be built and maintained here.
- **−** MCP spec changes (e.g. the stateless 2026-07-28 revision) require SDK upgrades.

## Risk

Medium — protocol churn. Mitigation: pinned SDK version; tool contract tests.

## Rollback

Tools are plain functions behind an MCP adapter; they can be exposed through another transport by replacing the adapter. Third-party servers may be admitted later through a per-server security review (Phase 8).
