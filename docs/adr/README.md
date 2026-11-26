# Architecture Decision Records

Decisions that are expensive to reverse. Format and approval flow come from agent-playbook:

- Format: [`templates/software/architecture-decision-record.md`](https://github.com/eerenyilmazz/agent-playbook/blob/main/templates/software/architecture-decision-record.md)
- Approval: [`roles/decision-maker/adr-approval.md`](https://github.com/eerenyilmazz/agent-playbook/blob/main/roles/decision-maker/adr-approval.md)

Rules: files are named `NNNN-short-title.md`, numbered sequentially and never reused; at most one page; accepted ADRs are immutable and are changed only by a superseding ADR.

## Index

| ADR | Title | Status |
| --- | --- | --- |
| 0001 | [TypeScript end-to-end; modular monolith on NestJS](0001-typescript-end-to-end-nestjs-monolith.md) | accepted |
| 0002 | [PostgreSQL with pgvector as the single data store](0002-postgresql-pgvector-single-store.md) | accepted |
| 0003 | [First-party MCP servers for tool and device integration](0003-first-party-mcp-servers.md) | accepted |
| 0004 | [Permission enforcement outside the model; content-based taint](0004-permission-engine-and-content-based-taint.md) | accepted |
| 0005 | [Explicit-only memory writes in v0.1; scoped memory](0005-explicit-scoped-memory-writes.md) | accepted |
| 0006 | [Manual model selection before automatic routing](0006-manual-model-selection-first.md) | accepted |
| 0007 | [Defer Redis, Tauri, voice and external actions beyond v0.1](0007-defer-redis-tauri-voice-external-actions.md) | accepted |
| 0008 | [Authenticated localhost backend and loopback-only services](0008-authenticated-localhost-loopback-services.md) | accepted |
| 0009 | [Device connectivity without listening ports](0009-device-connectivity-without-listening-ports.md) | accepted |
| 0010 | [Bind approvals to a verified fingerprint](0010-bind-approvals-to-verified-fingerprint.md) | accepted |
| 0011 | [Svelte 5 for the frontend](0011-svelte-5-frontend.md) | accepted |
