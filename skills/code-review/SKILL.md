---
name: code-review
description: Evidence-based review of a code change for correctness, security, data integrity, concurrency, and regression risk.
---

# Code review — operational procedure

## Inputs and scope
Request the base/head diff, repository conventions, product behavior, and test commands. If these are unavailable, state exactly what was inspected. Never imply a whole-repository review from one diff.

## Workflow
1. **Build a change map.** Identify changed public interfaces, callers, state owners, storage boundaries, network calls, permissions, and migrations. Inspect adjacent code before evaluating the diff.
2. **Enumerate invariants.** Examples: balances reconcile; IDs are unique; operations are idempotent; cancellation cannot commit stale results; auth checks occur server-side. Derive invariants from code/spec, not imagination.
3. **Trace risky paths.** For each new path follow success, invalid input, partial failure, retry, concurrent execution, and rollback. Pay attention to time zones, money precision, ordering, serialization, and compatibility.
4. **Prove or qualify findings.** Identify a concrete input or interleaving and the expected versus actual outcome. Prefer a failing test or executable reproduction. If only plausible, label it a hypothesis and explain what evidence is missing.
5. **Assess test quality.** Inspect assertions, fixtures, negative cases, and whether tests would fail for the identified defect. Don't equate coverage percentage with correctness.
6. **Report actionable findings only.** Don't bury functional bugs under style advice.

## Severity rubric
- **P0:** Immediate exploitable or irreversible widespread harm; stop rollout.
- **P1:** Serious production correctness/security/data-loss defect, likely under realistic conditions.
- **P2:** User-visible defect, reliability regression, or meaningful edge-case failure.
- **P3:** Low-impact but demonstrable defect; optional follow-up.

## Output contract
For each finding provide: `[P#] title`, precise file/line, **trigger**, **observed consequence**, **evidence**, **minimal fix**, **regression test**. Sort by severity. Then report tests actually run, tests not run, residual uncertainty. If none, write “No confirmed findings” rather than “looks good.”

## Example — double submit
Diff: payment button launches a request but stays enabled. Two taps can issue two non-idempotent charges.
Finding: `[P1] Prevent duplicate charge submission — CheckoutView.swift:88`.
Trigger: tap twice before first response. Consequence: two charges. Evidence: no in-flight guard or idempotency key in request path. Fix: server-enforced idempotency key; disable duplicate local submission as defense in depth. Test: two concurrent submits with same key produce one charge.

## Review checklist
- Authorization boundary and sensitive data logging
- Input validation and injection surfaces
- Partial writes, transaction isolation, and retries
- Resource lifecycle, cancellation, and stale responses
- Backwards compatibility and migration rollback
- Deterministic tests for discovered failures

Do not invent line numbers, test results, or product requirements.
