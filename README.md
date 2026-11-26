<p align="center">
  <img src="docs/assets/banner.svg" alt="Mell — remembers responsibly, acts only with permission" width="100%">
</p>

<p align="center">
  <a href="docs/PLAN.md"><img src="https://img.shields.io/badge/status-planning-FF5A1F?style=flat-square&labelColor=111110" alt="Status: planning"></a>
  <a href="docs/PLAN.md"><img src="https://img.shields.io/badge/plan-v0.6-EEEAE2?style=flat-square&labelColor=111110" alt="Plan v0.6"></a>
  <a href="docs/adr/"><img src="https://img.shields.io/badge/decisions-12_ADRs-EEEAE2?style=flat-square&labelColor=111110" alt="12 decision records"></a>
  <a href="https://github.com/eerenyilmazz/mell-assistant/actions/workflows/docs.yml"><img src="https://github.com/eerenyilmazz/mell-assistant/actions/workflows/docs.yml/badge.svg" alt="Docs CI"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/TypeScript-strict-1B1A18?style=flat-square&logo=typescript&logoColor=EEEAE2&labelColor=111110" alt="TypeScript">
  <img src="https://img.shields.io/badge/NestJS-backend-1B1A18?style=flat-square&logo=nestjs&logoColor=EEEAE2&labelColor=111110" alt="NestJS">
  <img src="https://img.shields.io/badge/Svelte_5-UI-1B1A18?style=flat-square&logo=svelte&logoColor=EEEAE2&labelColor=111110" alt="Svelte 5">
  <img src="https://img.shields.io/badge/Tauri_2-desktop-1B1A18?style=flat-square&logo=tauri&logoColor=EEEAE2&labelColor=111110" alt="Tauri 2">
  <img src="https://img.shields.io/badge/PostgreSQL-pgvector-1B1A18?style=flat-square&logo=postgresql&logoColor=EEEAE2&labelColor=111110" alt="PostgreSQL with pgvector">
  <img src="https://img.shields.io/badge/Ollama-local-1B1A18?style=flat-square&logo=ollama&logoColor=EEEAE2&labelColor=111110" alt="Ollama">
  <img src="https://img.shields.io/badge/MCP-2026--07--28-1B1A18?style=flat-square&labelColor=111110" alt="MCP 2026-07-28">
</p>

<h3 align="center">A local-first personal AI assistant that remembers responsibly<br>and acts on your computers only with permission.</h3>

<p align="center">
  <a href="#why-mell">Why MELL</a> ·
  <a href="#architecture">Architecture</a> ·
  <a href="#how-a-turn-works">How a turn works</a> ·
  <a href="#security-model">Security</a> ·
  <a href="#roadmap">Roadmap</a> ·
  <a href="docs/PLAN.md"><b>Full plan</b></a>
</p>

---

> [!NOTE]
> **MELL is in the planning phase.** There is no runnable code yet. The design, decisions and threat model are complete enough to start Phase 0; see the [project plan](docs/PLAN.md).

## Why MELL

Most assistants either forget everything or remember things you never asked them to, and agents that can touch your files tend to trust whatever text they read. MELL is designed around the opposite defaults.

<p align="center">
  <img src="docs/assets/features.svg" alt="Three principles: governed memory, permission first, local and Turkish-first" width="100%">
</p>

<p align="center">
  <img src="docs/assets/ui-preview.svg" alt="Concept of the Mell command surface: an editorial thread with tool receipts, a delete blocked by policy and an approval bound to launching IntelliJ IDEA; a context column with memory in use, system, devices and safeguards; a command bar in listening state" width="100%">
  <br>
  <sub><i>Concept of the command surface — what you asked, what Mell did, and the one decision it needs from you.</i></sub>
</p>

## Ask for anything

Mell is not limited to chat. Abilities arrive as capability packs, so the list keeps growing without changing the core:

| You say | Mell does | Policy |
| --- | --- | --- |
| "Spotify'dan biraz lo-fi aç" | Starts playback through the media pack | Control — automatic once you allow the pack |
| "Şu YouTube videosunu aç" | Opens the link in your browser | Launch |
| "IntelliJ'de MELL projesini aç" | Launches the IDE with the project on your Windows host | Launch |
| "Sesi yarıya indir" | Sets system volume | Control |
| "İndirilenler'deki eski PDF'leri sil" | Lists files, then stops: deleting after reading untrusted file names needs a clean, approved turn | Destructive |

Catalog, rules and phases: [plan, Section 9.8](docs/PLAN.md#98-capabilities--ask-for-anything).

## Architecture

<p align="center">
  <img src="docs/assets/architecture.svg" alt="Architecture: Windows host with UI, NestJS backend, Ollama, PostgreSQL and host MCP server; Mac with UI client and outbound device connector; optional cloud model" width="100%">
</p>

| Principle | In practice |
| --- | --- |
| **One host, one source of truth** | The backend on the Windows host holds all state, credentials and policy. |
| **Nothing listens that doesn't have to** | Ollama and PostgreSQL bind to loopback; device MCP servers open no port at all. |
| **Modular monolith** | NestJS modules with enforced boundaries — no microservices to operate. |
| **Replaceable models** | All model access goes through internal ports; local by default, cloud opt-in. |

<details>
<summary><b>Request flow (sequence diagram)</b></summary>

```mermaid
sequenceDiagram
    autonumber
    actor U as User
    participant UI as Svelte UI
    participant BE as Backend
    participant MEM as Memory
    participant PE as Permission Engine
    participant OL as Ollama
    participant D as Device MCP

    U->>UI: Message (Turkish)
    UI->>BE: POST message · Idempotency-Key · Correlation-Id
    BE->>MEM: Hybrid retrieval (scope + global)
    MEM-->>BE: Confirmed facts as data
    BE->>OL: Stream with allowed tools
    OL-->>BE: Tool proposal
    BE->>PE: Evaluate (class, scope, taint)
    PE->>D: Execute if allowed or approved
    D-->>BE: Result (untrusted, taints turn)
    BE->>OL: Continue with result
    OL-->>UI: Tokens over SSE
```

</details>

## How a turn works

Every message goes through the same seven deterministic stages. The model decides *what to say*; code decides *what is allowed to happen*.

<p align="center">
  <img src="docs/assets/turn-pipeline.svg" alt="Turn pipeline: intake, context, generate, policy, execute, respond, record, with a tool proposal loop" width="100%">
</p>

## Security model

MELL holds personal data and can act on your machines, so security is part of the core design. The key idea: an agent with private data, untrusted content and a way to send data out can be turned against its user — so MELL removes the third capability whenever untrusted content is in play.

<p align="center">
  <img src="docs/assets/security-model.svg" alt="Lethal trifecta with external communication blocked while a turn is tainted, and six defence layers" width="100%">
</p>

Threats, mitigations and the tests that verify them: [threat model](docs/security/threat-model.md) (STRIDE per boundary, OWASP Top 10 for Agentic Applications 2026 mapping, abuse cases).

## Technology stack

| Layer | Choice | Why |
| --- | --- | --- |
| Language | TypeScript (`strict`), end-to-end | One language for backend, UI, MCP servers and desktop shell ([ADR 0001](docs/adr/0001-typescript-end-to-end-nestjs-monolith.md)) |
| Backend | Node.js LTS · NestJS · Zod | Modules, DI and guards that mirror the layered design |
| Data | PostgreSQL · pgvector · Drizzle | Facts, vectors and Turkish full-text in one store ([ADR 0002](docs/adr/0002-postgresql-pgvector-single-store.md)) |
| AI | Vercel AI SDK behind internal ports · Ollama | Provider-agnostic; local models first ([ADR 0006](docs/adr/0006-manual-model-selection-first.md)) |
| Tools | Model Context Protocol, official TypeScript SDK | First-party servers with pinned definitions ([ADR 0003](docs/adr/0003-first-party-mcp-servers.md)) |
| UI | Svelte 5 · SvelteKit (static) · shadcn-svelte · Tailwind | Fine-grained updates for token streaming ([ADR 0011](docs/adr/0011-svelte-5-frontend.md)) |
| Desktop | Tauri 2 | Small footprint on Windows and macOS |
| Voice *(Phase 5)* | LiveKit Agents (Node.js), self-hosted | Same language, measured latency budget |
| Quality | Vitest · Testcontainers · Playwright · dependency-cruiser · OpenTelemetry | Tests, architecture rules and per-stage traces |

## Roadmap

<p align="center">
  <img src="docs/assets/roadmap.svg" alt="Roadmap with nine phases; phases 0 to 2 form v0.1 followed by a quality gate" width="100%">
</p>

<details>
<summary><b>What v0.1 includes</b></summary>

- Local Turkish chat with streaming, history, cancellation and idempotent requests
- Explicit, scoped memory with a Memory Center (view, edit, export, delete)
- Manual model selection; one resident local model plus embeddings
- Read-only device tools (`filesystem.list`, `filesystem.read`, `system.status`) behind the Permission Engine
- Activity log of every tool call, approval and memory change

Exit criteria for each phase: [plan, Section 15](docs/PLAN.md#15-delivery-phases).

</details>

## Documentation

| | Document | What you'll find |
| --- | --- | --- |
| 📘 | [Project plan](docs/PLAN.md) | Scope, prior-art review, architecture, permission model, memory, voice, data model, evaluation, phases, risks |
| 🧭 | [Decision records](docs/adr/) | Twelve ADRs with options, risks and rollback |
| 🛡️ | [Threat model](docs/security/threat-model.md) | Assets, adversaries, STRIDE, OWASP Agentic Top 10, security tests |
| 📖 | [Glossary](docs/GLOSSARY.md) | Taint, approval binding, turn pipeline and other terms |
| 🗂️ | [Documentation index](docs/README.md) | Everything else, organised by what you need |

## Run

Not runnable yet. Commands for local start, tests and required environment variables are added here in Phase 0 ([plan](docs/PLAN.md#phase-0--foundation)).

## Owner

Eren ([@eerenyilmazz](https://github.com/eerenyilmazz))

## Playbook

This project follows [agent-playbook](https://github.com/eerenyilmazz/agent-playbook). Agents and contributors load its rules as described in [`AGENTS.md`](AGENTS.md).

- Templates: software, desktop, web
- Roles: backend, frontend, qa-security, security-reviewer, code-reviewer, decision-maker, technical-writer, devops-cloud
- Stack: TypeScript (strict) on Node.js LTS · NestJS · Drizzle · PostgreSQL + pgvector · Vercel AI SDK · MCP TypeScript SDK · Svelte 5 · Tauri 2

### Overrides

Only values that differ from the playbook defaults.

| Rule | Default | This project | Reason |
| --- | --- | --- | --- |
| API p95 read latency | 300 ms | 300 ms, but chat is measured as time-to-first-token (baseline set in Phase 1) | Streaming responses; total duration depends on answer length |
| API p95 write latency | 800 ms | 800 ms, excluding model calls | Model latency is tracked separately per model |
| Browser matrix | latest 2 majors | WebView2 (Windows) and WKWebView (macOS) via Tauri; latest Chrome for development | Desktop shell, single user |
| Sprint length | 1–2 weeks | No sprints; phase-based delivery with exit criteria | Single developer, part-time |
| Release watch window | 60 min | Not applicable until a packaged release exists | No production deployment |
| Severity response times | Sev1 now / Sev2 1 h / Sev3 next day | Best effort | Personal project |

### Out of scope

See [Non-Goals](docs/PLAN.md#42-non-goals-v01): microservices, model training, third-party plugins or MCP servers, messaging-channel integrations, unattended destructive or external actions.

## Contributing

Pull requests only; `main` is protected. Read [`CONTRIBUTING.md`](CONTRIBUTING.md). Decisions are recorded in [`docs/adr/`](docs/adr/). Report vulnerabilities as described in [`SECURITY.md`](SECURITY.md).

## License

Not licensed yet. Until a license is added, all rights are reserved by the author.

---

<p align="center">
  <sub>Designed in the open · documentation-first · every decision recorded</sub>
</p>
