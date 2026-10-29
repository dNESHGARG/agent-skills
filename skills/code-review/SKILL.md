---
name: code-review
description: Review changes for correctness, security, maintainability, and missing tests, prioritizing reproducible defects.
---

# Code review

1. Establish the change's intended behavior from the diff, tests, and surrounding code. Do not assume undocumented requirements.
2. Trace inputs, state changes, failure paths, and externally visible effects.
3. Look for demonstrable correctness, security, data-loss, performance, and concurrency defects. Distinguish confirmed findings from hypotheses.
4. For each finding, identify the exact location, triggering scenario, impact, and smallest safe correction. Suggest a regression test.
5. Run relevant tests when tools are available; never claim to have run tests you did not run.
6. Return findings ordered by severity, followed by test gaps and a concise summary. If no actionable defects are found, say so and note remaining uncertainty.

Avoid stylistic nitpicks unless they materially affect maintainability. Do not introduce changes without authorization.
