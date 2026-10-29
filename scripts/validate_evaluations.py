"""Check that each evaluation case has a source fixture and expected findings."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
cases = json.loads((root / "evaluations" / "cases.json").read_text())["cases"]
for case in cases:
    assert (root / "evaluations" / case["file"]).is_file(), case["id"]
    assert case["skills"] and case["expected"], case["id"]
    for skill in case["skills"]:
        assert (root / "skills" / skill / "SKILL.md").is_file(), skill
print(f"Validated {len(cases)} evaluation fixtures")
