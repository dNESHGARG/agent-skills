---
name: concurrency-audit
description: Audit concurrent code for races, reentrancy, deadlocks, cancellation, and resource lifecycle defects.
---

# Concurrency audit

1. Map tasks, threads, actors, queues, shared state, and ownership boundaries.
2. Mark every suspension, callback, lock acquisition, and state mutation.
3. Examine check-then-act sequences, stale results, ordering assumptions, lock cycles, cancellation propagation, and shutdown behavior.
4. Describe a concrete interleaving for each suspected issue; distinguish theoretical hazards from demonstrated failures.
5. Recommend minimal synchronization or structural changes, preserving throughput where possible.
6. Suggest deterministic tests, stress tests, and instrumentation. Report which checks were actually executed.

Language-specific rules take precedence over generic advice; do not assume actors eliminate reentrancy.
