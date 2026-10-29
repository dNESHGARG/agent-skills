# Skill evaluations

The fixtures in this directory contain deliberately defective code. They are not examples to copy into production.

## Evaluation procedure

1. Give a reviewer only the selected fixture and its task description, not the expected findings.
2. Ask for findings using the relevant skill's output contract.
3. Compare with `expected-findings.md` using the rubric below.
4. Record false positives, missing defects, evidence quality, and suggested regression tests.
5. Repeat after every substantial skill change.

## Scoring rubric (per fixture)

- 2 points: correctly identifies root cause and a concrete triggering scenario.
- 1 point: severity is proportionate to impact.
- 1 point: proposed correction preserves the required invariant.
- 1 point: suggests a regression test that would fail before the fix.
- Subtract 1 point for each unsupported high-severity finding.

These are human-review criteria, not automated accuracy claims. The current suite is small and synthetic; real pull-request evaluation is still needed.
