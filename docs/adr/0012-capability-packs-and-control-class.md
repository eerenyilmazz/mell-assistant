# 0012. Capability packs and the Control action class

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

The owner wants to ask MELL for anything — play music on Spotify, open a YouTube video, open a project in IntelliJ, change the volume — and expects the list to keep growing. The v0.5 design had only read-only tools and action classes that put every third-party call in External, which would require approval for "pause the music" (PLAN.md 9.2, 9.8).

## Decision

Abilities are delivered as first-party capability packs: MCP servers that declare their tools, an action class per tool, output taint behaviour, credentials (OS secret store) and supported devices. A new **Control** class covers structured state changes in the user's own apps and accounts and is automatic once a pack is pre-approved. Free-text parameters sent to a third party are allowed in clean turns up to 120 characters and treated as External (blocked) in tainted turns.

## Options

- Hard-code integrations in the backend — every new ability changes the core and its tests.
- Allow third-party MCP servers and plugins — fastest growth, but the main attack surface found in prior art (ADR 0003).
- Keep all third-party calls in External — safe, but approval prompts for "next track" make the assistant unusable.
- Do nothing — MELL stays a chat with file reads.

## Consequences

- **+** New abilities without touching the core or the interface; each is reviewed once, in its own PR.
- **+** Everyday commands run without prompts; risky ones still stop at the policy engine.
- **−** Each pack must be built and maintained here, including provider API changes (e.g. Spotify's 2026 Development Mode limits).
- **−** More tools per turn; requires per-turn tool selection to keep local tool calling reliable.

## Risk

Medium — a misclassified tool could act without approval. Mitigation: action class and `structured-only` flag reviewed in the pack's PR; threat-model tests SEC-11 and SEC-12.

## Rollback

Disable a pack in the `capabilities` table; its tools disappear from the tool list immediately. Removing the Control class requires a superseding ADR and reclassifying tools as External.
