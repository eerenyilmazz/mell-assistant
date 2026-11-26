# Glossary

Terms as used in MELL's documentation. Plan sections are in parentheses.

| Term | Meaning |
| --- | --- |
| **Action class** | Category of a tool call that decides its default policy: read, launch, write, destructive, external, financial (9.2). |
| **Approval binding** | The fingerprint an approval is tied to — tool definition hash, canonical arguments hash, resolved scope, device, single-use id, expiry — re-verified immediately before execution (9.4). |
| **Candidate (memory)** | A proposed memory entry that is not yet confirmed and is never used as a fact (10.3). |
| **Confirmed (memory)** | A memory entry the user created or explicitly confirmed; the only kind injected as fact (10.3). |
| **Correlation id** | Identifier assigned to a turn and propagated to every model call, tool call, approval, log line and span it causes (6.9). |
| **Device connector** | Process on a non-host device that opens an outbound, authenticated connection to the backend and carries MCP messages for that device's MCP server (6.3). |
| **Hybrid retrieval** | Memory search that combines vector similarity and full-text search, fused by reciprocal rank fusion, after metadata filtering (10.9). |
| **Lethal trifecta** | The combination of access to private data, exposure to untrusted content and the ability to communicate externally, which enables data exfiltration through prompt injection (3.1). |
| **MCP** | Model Context Protocol; the standard protocol MELL uses between the backend and device tool servers (6.3). |
| **Permission Engine** | Deterministic code that decides whether a proposed tool call is allowed, denied or needs approval; the model never decides (9.1). |
| **Pinned tool definition** | A tool's name, description and schema approved by the user and stored with a hash; a changed hash disables the tool (9.6). |
| **Resolved scope** | The concrete targets of an action as shown to the user, for example absolute paths with size and modification time (9.4). |
| **Scope (memory)** | A user-defined memory space such as a project; retrieval uses the active scope plus `global` (10.2). |
| **Structured-only tool** | A tool whose outputs are all typed values produced by first-party code; its results do not taint a turn (9.3). |
| **Superseded (memory)** | A memory entry replaced by a newer one; kept for history and never injected as current (10.4). |
| **Taint** | Per-turn flag set when untrusted content enters the context; restricts what actions the turn may take (9.3). |
| **Tool poisoning** | Malicious instructions hidden in a tool's metadata, such as its description (3.1). |
| **TTFT** | Time to first token: delay between sending a request to a model and receiving its first output token (7.2). |
| **Turn** | One user input and everything MELL does in response; the unit of correlation, taint, cancellation and audit (6.5). |
| **Turn pipeline** | The seven fixed stages every turn passes through: intake, context build, generate, policy, execute, respond, record (6.5). |
