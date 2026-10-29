# Expected findings — evaluator-only answer key

**Keep this file hidden during blind reviews.**

## stale-search.ts
P2: earlier search response arrives last and overwrites latest query results. Use a request generation guard. Test with controlled deferred promises. Do not misclassify as a multithreaded data race.

## fixtures/duplicate-charge.ts
P1: two calls can create two charges for one checkout. Require server-enforced idempotency keyed to a logical payment. Test concurrent requests with the same key. Disabling the button alone is insufficient.

## fixtures/actor-reentrancy.swift
P1: two spend(80) operations can both pass the guard before await and overdraw. Reserve funds before suspension with compensation, or verify then atomically check and decrement without suspension. Actor isolation does not eliminate reentrancy.

## fixtures/cache-key.py
P2: cache key omits namespace, so different namespaces sharing item IDs can return incorrect cached values. Key by (namespace, item_id). Test with two namespaces and the same item ID.

## Scoring
Per case: root cause and trigger (2), severity (1), invariant-preserving fix (1), regression test (1). Deduct 1 per unsupported high-severity finding. Do not claim benchmark scores without executing reviewer evaluations.
