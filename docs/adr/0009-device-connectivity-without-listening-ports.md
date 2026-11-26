# 0009. Device connectivity without listening ports

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

v0.4 required device MCP servers to bind to loopback while expecting the Windows backend to reach the Mac's MCP server over the private network — a contradiction found in review. Devices also sleep, change networks and sit behind NAT (PLAN.md 6.3).

## Decision

No device MCP server opens a listening port. On the host, the backend runs the MCP server as a child process over stdio. On every other device, a device connector opens an outbound WebSocket over the private network to the backend, authenticates with a per-device credential and key, and carries MCP messages for the local MCP server. The connector also enforces its own local allow-list.

## Options

- Mac MCP server listening on the tailnet interface with mutual TLS — works, but adds a listening service on a laptop and a second certificate lifecycle.
- Mac MCP server on loopback with an SSH or VPN tunnel from the host — extra moving parts; host must reach the laptop.
- Reverse proxy or public relay — exposes device control beyond the private network.
- Do nothing — the v0.4 contradiction remains and Mac tools cannot work.

## Consequences

- **+** No port to scan or hijack on any device; works behind NAT and on changing networks.
- **+** Devices are revocable individually; a revoked device cannot reconnect.
- **+** Defence in depth: the device allow-list holds even if the backend is compromised.
- **−** Requires a custom MCP transport (JSON-RPC over the authenticated WebSocket) instead of an off-the-shelf HTTP transport.
- **−** Connector lifecycle (pairing, reconnect, backoff) must be built.

## Risk

Medium — custom transport code. Mitigation: transport conformance tests against the SDK; port scan of the Mac in the Phase 3 exit criteria.

## Rollback

Switch the Mac to the tailnet-bound mutual-TLS option; tool code is unchanged because only the transport differs.
