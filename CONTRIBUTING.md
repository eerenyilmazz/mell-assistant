# Contributing

MELL follows [agent-playbook](https://github.com/eerenyilmazz/agent-playbook). Its git, documentation and review rules apply in full; this file only adds what is specific to this repository.

## Workflow

1. Branch from `main`: `feature/<short-name>`, `fix/<short-name>` or `docs/<short-name>`. `main` is protected: no direct push, no force push.
2. Make one logical change. Keep the PR under 400 changed lines where possible; if not, explain why in the PR body.
3. Commit with [Conventional Commits](https://www.conventionalcommits.org/), for example `docs(plan): align ER diagram with schema` or `docs(adr): add 0011 hybrid retrieval`. Rules: playbook `company/git-and-versioning.md`.
4. Run the checks below and open a pull request using the template. State the risk level, test evidence, rollback and whether anything is breaking.
5. CI must pass and the code owner must approve. Squash merge.

## Checks

```bash
npx --yes markdownlint-cli2@0.24.2 "**/*.md"
```

CI additionally checks links with lychee. Mermaid diagrams must parse with Mermaid 11; check them in the GitHub preview or with the Mermaid Live Editor before opening the PR.

## Changing the plan

- `docs/PLAN.md` is versioned in its header (`Draft v0.N`). A content change bumps the version, updates the *Changes* line and adds a `CHANGELOG.md` entry.
- A change to a decision recorded in an ADR requires a new ADR that supersedes it.
- The data model is edited in the table list, the ER diagram and the schema notes together.

## Decisions (ADRs)

- Format: playbook `templates/software/architecture-decision-record.md`. Approval: playbook `roles/decision-maker/adr-approval.md`.
- Files: `docs/adr/NNNN-short-title.md`, numbered sequentially, never reused, at most one page.
- Open the ADR as `proposed` in its own PR; it becomes `accepted` on merge. No irreversible implementation before acceptance.

## Documentation style

- English, short sentences, active voice. Tables and diagrams over long prose.
- One fact in one place; link instead of copying.
- Keep the four documentation types separate (tutorial, how-to, reference, explanation). See [`docs/README.md`](docs/README.md).

## Security

Do not open public issues for vulnerabilities. See [`SECURITY.md`](SECURITY.md).
