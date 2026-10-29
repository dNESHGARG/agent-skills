---
name: bug-investigation
description: Reproduce and isolate bugs using competing hypotheses, instrumentation, bisecting, and regression tests.
---

# Bug investigation — evidence ladder

## 1. Define the failure
Record observed/expected behavior, first known bad version, environment, frequency, impact, and reproducible inputs. Separate facts from reporter interpretations. Preserve logs and relevant correlation IDs; redact secrets.

## 2. Build a hypothesis table
For each hypothesis capture **prediction**, **discriminating experiment**, **result**, and **confidence**. Favor experiments that eliminate multiple hypotheses cheaply.

| Hypothesis | Prediction | Experiment |
|---|---|---|
| Cache key collision | Wrong data only after visiting another account | Log sanitized cache key and compare isolated account sessions |
| Stale async response | Rapid switching reproduces; slow switching does not | Delay first response and inspect request sequence |
| Server corruption | Raw API payload already wrong | Compare server response with rendered model |

Do not treat correlation as root cause.

## 3. Isolate the boundary
Reproduce with smallest input; bisect commits or feature flags if feasible. Trace input -> parse -> transform -> state -> render or storage. Instrument timestamps and request IDs; avoid changing timing so much that the bug disappears.

## 4. Establish causality
A strong diagnosis has: minimal reproduction, precise mechanism, intervention that removes failure, and regression test that fails before fix and passes after. When one is missing, report confidence explicitly.

## 5. Fix safely
Prefer the smallest fix that restores the invariant. Check adjacent paths, retries, data migration, and compatibility. Include rollback plan for risky changes.

## Example — stale search results
User types “ca”, then “cat”; the slower “ca” response arrives last and overwrites “cat”.
- Experiment: fake network responses; release second response before first.
- Root cause: completion order used as request order.
- Fix: associate monotonic request ID with each search and apply only the latest response; cancellation can save work but is not the sole correctness guard.
- Regression: deterministic deferred promises resolved in reverse order; assert final results match “cat”.

## Deliverable
**Symptom**, **reproduction**, **root cause/evidence**, **fix**, **regression coverage**, **remaining risks**, **tests actually run**. Never fabricate traces or claim tests passed without execution.
