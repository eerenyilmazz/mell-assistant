# Documentation

Index of MELL's documentation, organised by what the reader needs ([Diátaxis](https://diataxis.fr/)): learn, do a task, look up a fact, or understand why.

| Need | Type | Documents |
| --- | --- | --- |
| Understand what MELL is and why it is designed this way | Explanation | [`PLAN.md`](PLAN.md) — scope, prior art, architecture, security model, memory design, phases |
| Look up a decision and its rationale | Reference | [`adr/`](adr/) — Architecture Decision Records |
| Look up a term | Reference | [`GLOSSARY.md`](GLOSSARY.md) |
| Contribute a change | How-to | [`../CONTRIBUTING.md`](../CONTRIBUTING.md) |
| Work in the repo as a coding agent | How-to | [`../AGENTS.md`](../AGENTS.md) |
| Report a vulnerability | How-to | [`../SECURITY.md`](../SECURITY.md) |
| Run MELL locally | Tutorial | Added in Phase 0 |

## Planned documents

Written when their phase begins, not before, so they describe real behaviour:

| Document | Phase | Content |
| --- | --- | --- |
| `security/threat-model.md` | 0 | Trust boundaries, STRIDE per boundary, OWASP Agentic Top 10 mapping, mitigations as tests |
| `api/openapi.yaml` | 1 | REST and SSE contract, versioned with the code |
| `benchmarks/` | 1–2 | Measured model, embedding and latency results |
| `runbook.md` | 3 | Start, stop, backup, restore, device pairing and revocation |
| `voice.md` | 5 | Measured voice pipeline and provider decision |

## Conventions

- English; Markdown; diagrams in Mermaid.
- One fact in one place: other documents link to the plan or an ADR instead of restating it.
- Project-wide rules come from [agent-playbook](https://github.com/eerenyilmazz/agent-playbook) and are not copied here.
