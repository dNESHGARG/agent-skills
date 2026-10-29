# Agent Skills

Reusable engineering investigation and review procedures. Each skill specifies concrete evidence requirements, decision points, reproducible examples, and a structured deliverable. These are **not** substitutes for repository-specific context or actually running tests.

## Available skills

| Skill | When to use | Key artifact |
|---|---|---|
| [Code review](skills/code-review/SKILL.md) | Before merging risky changes | Prioritized, reproducible findings |
| [Bug investigation](skills/bug-investigation/SKILL.md) | Intermittent or hard-to-reproduce failures | Hypothesis table and verified root cause |
| [Concurrency audit](skills/concurrency-audit/SKILL.md) | Shared state, async code, worker pools | Task interleaving and invariant violations |
| [Swift concurrency review](skills/swift-concurrency-review/SKILL.md) | Swift 6 migrations and async SwiftUI | Isolation map and lifecycle analysis |

## Validation

```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

The validator checks naming, metadata, and minimum document structure. It **does not** certify the technical correctness of skill instructions. GitHub Actions runs the checks on pushes and pull requests.

## Design principles

- Claims must be tied to inspected code, test output, or a labeled hypothesis.
- A review finding includes a trigger, observable consequence, evidence, minimal fix, and regression test.
- Cancellation, concurrency, and data-integrity analysis should demonstrate concrete interleavings.
- No invented line numbers, logs, benchmarks, or test outcomes.

## Next

Add repository-backed evaluation fixtures with expected findings and false-positive checks; run skills against real pull requests and compare their outputs with a review rubric.
