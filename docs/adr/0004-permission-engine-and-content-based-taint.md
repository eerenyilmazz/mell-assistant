# 0004. Permission enforcement outside the model; content-based taint

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

An agent with private data, untrusted content and a way to communicate externally can be made to exfiltrate data by prompt injection (the "lethal trifecta"). Guardrail models reduce but do not remove this. v0.4 also exempted results from a "trusted directory", although file names and contents in an allowed directory can carry injected instructions (PLAN.md 9.3).

## Decision

A deterministic Permission Engine decides every tool call; the model only proposes. Each turn carries a taint flag set by the provenance of content entering the context — any file name or content, web page, document, import or free-text tool result taints the turn. In a tainted turn, external and destructive actions are blocked in v0.x and memory writes become unconfirmed candidates.

## Options

- Rely on the system prompt and model judgement — known to fail under injection.
- Guardrail/classifier only — probabilistic; misses are silent.
- Taint by directory permission (v0.4) — treats attacker-controlled files as trusted.
- Remove tools entirely — no useful assistant.

## Consequences

- **+** Exfiltration leg of the trifecta is removed by construction while a turn is tainted.
- **+** Behaviour is testable with a prompt-injection corpus (PLAN.md 14).
- **−** Many useful turns become tainted (any file read), limiting chained actions until approval UX matures.
- **−** Every new tool needs an action class and a `structured-only` review.

## Risk

Low for security, medium for usability. Mitigation: measure how often tainted turns block legitimate tasks in Phase 2 and adjust UX, not the rule.

## Rollback

Policy is data plus code in one module; individual rules can be relaxed by a superseding ADR. The engine itself is not removable without reopening the trifecta.
