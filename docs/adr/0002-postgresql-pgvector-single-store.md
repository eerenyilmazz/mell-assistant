# 0002. PostgreSQL with pgvector as the single data store

Status: accepted
Date: 2026-11-26 · Deciders: Eren

## Context

MELL stores relational data (conversations, turns, approvals, audit) and vectors for memory retrieval. Memory deletion must remove the entry, its embedding and derived data atomically (PLAN.md 10.4). Full-text search in Turkish is also needed (10.9).

## Decision

Use one PostgreSQL instance with the pgvector extension for all persistent data, including embeddings and a generated `tsvector` column using the built-in `turkish` configuration. No separate vector database, cache or queue in v0.x.

## Options

- Separate vector database (Qdrant, Chroma, Milvus) — second store to back up and keep consistent; deletion no longer atomic.
- SQLite + vector extension — simpler to ship in a desktop app, but weaker concurrency and full-text options for Turkish; harder to move to a server later.
- Add Redis now — no documented need in v0.x.
- Do nothing — no store; not viable.

## Consequences

- **+** One backup, one migration tool, transactional deletes across facts and vectors.
- **+** Hybrid retrieval (vector + full-text) in a single SQL query path.
- **−** Requires running PostgreSQL (Docker) on the host machine.
- **−** Vector search performance is bounded by pgvector; acceptable at personal-assistant scale.

## Risk

Low — data volume for one user is small. Mitigation: index choice and recall measured in Phase 2 benchmarks.

## Rollback

Embeddings can be exported and loaded into a dedicated vector store behind `EmbeddingModelPort` and the memory repository; relational data stays in PostgreSQL.
