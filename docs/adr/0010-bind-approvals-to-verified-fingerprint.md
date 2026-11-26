# 0010. Bind approvals to a verified fingerprint

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

Approval dialogs show the user an exact scope (for example three files to delete). Between approval and execution, the tool definition, the arguments or the targets can change: a file is added to a folder, a pattern matches differently, a definition is updated, or an approval is replayed. Review of v0.4 identified this time-of-check/time-of-use gap (PLAN.md 9.4).

## Decision

Each approval is bound to a fingerprint: single-use approval id, tool definition hash, canonical arguments hash, resolved scope (paths with size and modification time, or content hashes for small files), device id, turn and correlation id, and a short expiry. The approval id is consumed atomically when execution starts; the device recomputes the resolved scope and aborts on any mismatch, then the user is asked again with the new scope.

## Options

- Approve by tool and arguments only — misses target changes between approval and execution.
- Approve once per tool or session — convenient, but widens every approval silently.
- Lock targets during approval — not possible across processes and devices in general.
- Do nothing — what runs may differ from what was approved.

## Consequences

- **+** What runs is exactly what the user approved, or nothing runs.
- **+** Replay, transfer to another device and scope widening are impossible.
- **−** Legitimate changes (a file touched by a sync tool) cause re-prompts.
- **−** Hashing large targets costs time; bounded by using size and modification time above 10 MB.

## Risk

Low. Mitigation: tests for mismatch, replay and expiry (PLAN.md 14.1, 14.4).

## Rollback

Fingerprint fields can be reduced by a superseding ADR; removing the binding entirely reopens the gap.
