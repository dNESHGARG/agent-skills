---
name: bug-investigation
description: Investigate a software bug from symptoms through reproducible root cause and verified regression test.
---

# Bug investigation

1. Record expected behavior, actual behavior, environment, and available logs.
2. Produce the smallest reliable reproduction. If reproduction is impossible, clearly label hypotheses.
3. Narrow the failing boundary with targeted instrumentation or tests, not broad speculative rewrites.
4. Identify the root cause and explain why it produces the observed behavior.
5. Implement the minimal correction only when requested, and add a regression test that fails before the fix and passes after.
6. Report evidence, residual risks, and any cases not tested.

Never invent logs, stack traces, test results, or reproduction steps.
