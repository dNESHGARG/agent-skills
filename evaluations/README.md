# Engineering review evaluation suite

Four deliberately defective fixtures across TypeScript, Swift, and Python cover stale async results, duplicate payment submissions, actor reentrancy, and cache-key collisions.

## Blind evaluation protocol

1. Select a case in `cases.json` and its assigned skill.
2. Give the reviewer only the fixture source and corresponding `SKILL.md`; withhold `expected-findings.md`.
3. Request the skill's structured findings, with concrete triggers and regression tests.
4. Score against the answer key: cause + trigger (2), severity (1), fix (1), test (1), minus 1 for unsupported high-severity findings.
5. Record false positives, missed findings, and disagreements across revisions.

## Validate

```bash
python scripts/validate_evaluations.py
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

This is a small synthetic evaluation suite, not evidence of performance on real pull requests. The validator checks fixture metadata, not AI detection accuracy.
