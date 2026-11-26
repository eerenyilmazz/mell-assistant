# AGENTS.md

Instructions for AI coding agents working in this repository. Humans: see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Rules source

This project follows [agent-playbook](https://github.com/eerenyilmazz/agent-playbook). Follow its protocol (`AGENTS.md` there) on every task:

- Load the playbook `company/` files with `scope: always`, then only the files matching the task:
  `python3 scripts/load.py --templates software,desktop,web --role <role> [--skill <skill>] --task "<task>"`
  (run inside a clone of agent-playbook).
- Project selection and overrides: [`README.md` → Playbook](README.md#playbook).
- Precedence: the user's explicit instruction → README overrides → playbook `company/` → templates → roles → skills. On conflict, follow the higher one and say so.
- Do not restate playbook rules in this repository; link to the playbook file instead.

## Current state

- Planning phase. There is no application code, no package manifest and no build. Do not scaffold code unless the task asks for it.
- [`docs/PLAN.md`](docs/PLAN.md) is the source of truth for scope and design. [`docs/adr/`](docs/adr/) holds decisions.

## Boundaries

- Never push to `main`, force-push, rewrite history or delete files without the owner's explicit approval. Work on a branch and open a pull request.
- Accepted ADRs are immutable. To change a decision, add a new ADR that supersedes it.
- Do not weaken a security rule in `docs/PLAN.md` (Sections 6.3, 6.8, 9, 10.6, 12) without an ADR.
- Do not add third-party MCP servers, plugins or dependencies to any plan or code without a justification line in the PR.
- Never put secrets, personal file paths or personal data in the repository; this repository is public.

## Editing docs/PLAN.md

- Bump the version and the *Changes* line in the header table, and add a `CHANGELOG.md` entry.
- The data model lives in three places that must change together: the table list and ER diagram (13.1), the schema notes (10.7) and, later, the migrations.
- Keep section numbers stable; README and ADRs link to them. If a heading changes, fix every link to it.
- Diagrams are Mermaid; tables over prose; English only.

## Definition of done (docs changes)

Run before reporting a docs task as done, and report the actual results:

```bash
npx --yes markdownlint-cli2@0.24.2 "**/*.md"   # pinned; uses .markdownlint-cli2.jsonc
```

- Every Mermaid block parses (Mermaid 11). If you cannot run a parser, say so; do not claim it passed.
- Relative links and `#anchors` resolve (CI runs lychee).
- PR body follows [`.github/pull_request_template.md`](.github/pull_request_template.md), including risk level and rollback.

## Reporting gaps

If a needed playbook rule is missing or wrong, end your output with:
`Playbook gap: <file or topic> — <what is missing or wrong> — <suggested fix>`
