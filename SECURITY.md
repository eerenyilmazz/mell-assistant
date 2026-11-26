# Security Policy

## Status

MELL is in the planning phase. There is no released software, so there are no supported versions yet. This policy applies to the design documents now and to code once it exists.

## Reporting a vulnerability

- **Do not open a public issue** for a security problem.
- Use GitHub's private vulnerability reporting for this repository (*Security* tab → *Report a vulnerability*). If that option is not available, open an issue titled `Security contact request` with no details, and the owner will reply with a private channel.
- Include what is affected (document section, component, version), how to reproduce or the reasoning, and the impact you expect.

## What to expect

- Acknowledgement within 7 days. This is a personal project maintained part-time; response times are best effort.
- Design flaws are fixed in `docs/PLAN.md` and, where a decision changes, in a new ADR.
- Credit in the fix's PR and `CHANGELOG.md` entry, unless you prefer otherwise.

## Scope

In scope:

- Weaknesses in the security design: permission engine, taint rules, approval binding, device connectivity, memory handling, network binding, supply-chain controls (`docs/PLAN.md` Sections 6.3, 6.8, 9, 10, 12).
- Once code exists: the backend, UI, device MCP servers and connectors, and their configuration.

Out of scope:

- Vulnerabilities in third-party services or models (report them to their vendors).
- Issues that require an already compromised operating system account on the user's machine.

## Design principles

MELL treats model output, tool results, file names and contents, and retrieved memory as untrusted, and enforces permissions in deterministic code outside the model. Details: [`docs/PLAN.md` Section 12](docs/PLAN.md#12-security-and-privacy). Threats, mitigations and the tests that verify them: [`docs/security/threat-model.md`](docs/security/threat-model.md).
