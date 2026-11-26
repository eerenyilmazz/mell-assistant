# 0011. Svelte 5 for the frontend

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

OD-5 left the frontend open between React and Angular. The owner set no language or framework preference and asked for the most logical and performant option. The UI runs inside a Tauri webview, and its dominant workload is appending streamed tokens to a growing message list (PLAN.md 6.7.1, 16.0).

## Decision

Build the UI with Svelte 5 (runes) and SvelteKit using the static adapter as a single-page app, with `@ai-sdk/svelte`, shadcn-svelte components copied into the repo, and Tailwind CSS. No global store or query library until a second use appears.

## Options

- React 19 — largest ecosystem and most complete AI SDK UI package; component re-render model and largest runtime are the weakest fit for per-token updates.
- Angular 20 — official AI SDK package and signals; larger runtime and more framework surface than the UI needs.
- SolidJS — performance comparable to Svelte; AI SDK support is community-maintained only.
- Do nothing — OD-5 blocks Phase 1.

## Consequences

- **+** Fine-grained updates and the smallest runtime among the candidates; fast start inside the webview.
- **+** Official AI SDK integration; common Tauri template.
- **−** Smaller component and hiring ecosystem than React; some chat-UI libraries exist only for React.
- **−** Svelte is new to the owner; Phase 1 includes the learning cost.

## Risk

Low — the UI is a client of the REST/SSE contract in `packages/contracts`. Mitigation: streaming-rendering rules (16.0) and a measured Phase 1 baseline.

## Rollback

Rewrite the UI in another framework against the same contract; backend and contracts are unaffected. Cost: the UI code written so far.
