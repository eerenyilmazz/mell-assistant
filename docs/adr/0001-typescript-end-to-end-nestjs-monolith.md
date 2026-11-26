# 0001. TypeScript end-to-end; modular monolith on NestJS

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

MELL needs a backend, a desktop UI, MCP servers on two operating systems and, later, a voice pipeline, built by one part-time developer. The first draft used Java/Spring Boot with an Angular UI. MCP support, LLM tooling and voice frameworks differ strongly between ecosystems (PLAN.md 6.7).

## Decision

Use TypeScript (`strict`) on Node.js LTS for every component, with the backend as a NestJS modular monolith. Shared contracts are Zod schemas in one package.

## Options

- Java 21 + Spring Boot + Spring AI — strongest existing skill; but three languages in the repo, Java MCP SDK not Tier 1, no native voice framework.
- Python + FastAPI — best local ML ecosystem; but weakest existing skill and still a second language for the UI.
- Microservices in any language — operational cost with no benefit for a single user.
- Do nothing (keep the Java draft) — keeps the costs above.

## Consequences

- **+** One language for backend, UI, MCP servers and desktop shell; shared types without code generation.
- **+** Tier 1 MCP SDK on the current spec; mature provider-agnostic LLM toolkit; LiveKit Agents has a Node SDK.
- **−** Highest supply-chain exposure (npm); requires the controls in PLAN.md 6.8.
- **−** Less backend experience in Node than in Java; NestJS reduces the gap.
- **−** ML pieces (Turkish embeddings, STT) run as external services, not in-process.

## Risk

Medium — delivery speed may drop while learning Node backend patterns. Mitigation: NestJS conventions, strict types, small Phase 0–1 scope; review after Phase 1.

## Rollback

All AI and storage access sits behind ports, so the backend can be rewritten in Java after Phase 1 at the cost of the backend code only; UI and contracts survive if exposed over the same REST/SSE API.
