# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Releases will use [Semantic Versioning](https://semver.org/) once code exists; until then, entries track versions of the project plan.

## [Unreleased]

### Changed

- Plan v0.5.2: frontend decided as Svelte 5 (ADR 0011, OD-5 closed); streaming-rendering rules for the chat UI (Section 16.0).

### Added

- Project governance: `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, pull request template, code owners, documentation index and glossary.
- Markdown lint and link checks in CI.
- Threat model: assets, adversaries, trust boundaries, STRIDE per boundary, OWASP Agentic Top 10 mapping, abuse cases and security tests.
- Plan v0.5.1: size, count and depth limits for read tools (Section 9.7); Section 12 links to the threat model.
- README sections required by agent-playbook: Run, Owner, Playbook, Overrides, Out of scope.

## [plan-v0.5] - 2026-11-26

### Changed

- Device MCP servers open no listening port: stdio on the host, outbound authenticated connector on other devices.
- Taint follows content provenance; file names and contents always taint.
- Voice latency budget made consistent: acceptance 1.3 s P50, stretch 0.9 s.
- Table list, ER diagram and schema notes aligned; `turns` table added.
- Engineering rules defer to agent-playbook; ADRs move to the playbook format in `docs/adr/`.

### Added

- Turn pipeline; correlation ids, idempotency, cancellation, timeouts and recovery states.
- Approval binding against time-of-check/time-of-use changes.
- Hybrid memory retrieval (pgvector + PostgreSQL `turkish` full-text).

### Security

- Removed the "trusted directory" exception from taint rules.
- Approvals are single-use and re-verified at execution.

## [plan-v0.4] - 2026-11-26

### Added

- Project plan `docs/PLAN.md` with prior-art review, architecture, permission model, memory design, voice, security, data model, evaluation, delivery phases, risks and open decisions.
- 18 Mermaid diagrams and UI wireframes.
- README with overview, architecture and roadmap; SVG banner.

### Changed

- Technology stack re-selected from Java/Spring Boot + Angular to TypeScript end-to-end (NestJS, AI SDK, MCP, React, Tauri).

[Unreleased]: https://github.com/eerenyilmazz/mell-assistant/compare/79ade8e...HEAD
[plan-v0.5]: https://github.com/eerenyilmazz/mell-assistant/pull/2
[plan-v0.4]: https://github.com/eerenyilmazz/mell-assistant/pull/1
