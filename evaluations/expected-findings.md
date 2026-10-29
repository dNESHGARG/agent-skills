# Expected findings (keep hidden during review)

## stale-search.ts

**P2: Older request overwrites newer search results.**
- Trigger: two overlapping `update` calls; first response resolves last.
- Invariant: results must reflect latest requested query.
- Evidence: no generation token, request identity, or guard before assigning results.
- Fix: increment a request generation before awaiting, and apply only if still current. Cancellation may improve efficiency but is not sufficient by itself.
- Regression: control promises, resolve the second first, then first; final state must correspond to the second query.
- False positive to avoid: claiming a JavaScript memory data race. The failure is a logical ordering race in async completions.

This fixture alone does not measure reviewer quality. Report any missed or unsupported findings.
