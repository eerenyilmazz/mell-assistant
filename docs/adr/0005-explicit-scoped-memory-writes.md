# 0005. Explicit-only memory writes in v0.1; scoped memory

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

Memory is MELL's main value and main liability. Large assistants have shown silent loss, silent modification and over-eager extraction of memories, and context from unrelated areas of life spilling together (PLAN.md 3.1). Persistent memory can also carry injected instructions into future sessions.

## Decision

In v0.1, memory is written only on explicit user instruction or in the Memory Center, and every entry is confirmed. Every entry belongs to a user-defined scope; retrieval uses the active scope plus `global`. Updates supersede instead of overwrite. Automatic extraction (Phase 4) produces candidates only.

## Options

- Automatic extraction from every conversation — high recall, high error rate, hard to audit.
- No persistent memory — removes MELL's main differentiator.
- Single global memory without scopes — simpler, but mixes work, personal and project context.
- Do nothing — same as no memory.

## Consequences

- **+** Every stored fact is something the user asked to store; easy to trust and audit.
- **+** Scopes prevent cross-context leakage and make retrieval cheaper.
- **−** Lower recall: facts the user never states explicitly are not remembered in v0.1.
- **−** More UI work (Memory Center, scope selection).

## Risk

Low. Mitigation: memory evaluation set (PLAN.md 14.2) gates Phase 2 and Phase 4.

## Rollback

Extraction can be enabled earlier by a superseding ADR; data model already supports candidates. Scopes can be collapsed into `global` by a migration.
