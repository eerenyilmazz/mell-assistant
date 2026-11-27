# 0013. Single Linux host

Status: accepted
Date: 2026-11-27 · Deciders: Eren

## Context

Up to plan v0.6, Mell ran on a Windows host (RTX 4070 Ti, 12 GB VRAM, 32 GB RAM) with a MacBook Air as a secondary client and second device (PLAN.md 5, 6.2, 6.3). The owner will not build or maintain the macOS side and wants the whole system on Linux. Supporting Windows only as a host for a single user adds a second platform adapter, a second packaging target and a remote-device path that nobody uses.

## Decision

Mell runs on **one Linux machine** — the same desktop, running Linux. It is the host and the only device in v0.x. Windows and macOS are removed from scope:

- The device MCP server has one platform adapter (Linux) and is reached over stdio (unchanged, ADR 0009).
- Tauri 2 is packaged for Linux only.
- No remote device and no private-network access in v0.x. If a remote client is added later (mobile), ADR 0009 and PLAN.md 12 items 3–4 apply unchanged.
- Distribution and desktop session (Wayland or X11) are an open decision (OD-8).

## Options

- Keep Windows host and macOS client — two platforms the owner will not maintain.
- Windows host only — the stack works, but Linux is the native platform for Node, PostgreSQL, Docker and Ollama, and the owner prefers it.
- Linux host plus Windows as a controlled second device (dual boot) — a second adapter and a remote path for a machine that is never online at the same time.

## Consequences

- **+** One platform to build, test and package; no remote-device code in v0.x.
- **+** Smaller attack surface: nothing listens on the network at all, not even the private network.
- **+** Native tooling for the stack (systemd, Docker, CUDA with Ollama) and standard desktop interfaces for capability packs (`xdg-open`, MPRIS over D-Bus, PipeWire, Secret Service).
- **−** Some desktop control (window switching, global input) may be limited under Wayland; each pack declares what works per session type.
- **−** Docker's published ports bypass host firewalls such as UFW; every published port must bind to `127.0.0.1` (PLAN.md 12).
- **−** When the machine is off, Mell is off. Acceptable for a single user at that machine; revisited with the mobile client (OD-1).

## Risk

Low — planning phase; no code exists. The security model is unchanged or stricter.

## Rollback

Add a superseding ADR that restores a platform; the MCP server's adapter boundary (PLAN.md 20) and ADR 0009 keep that path open.
