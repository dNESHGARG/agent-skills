#!/usr/bin/env python3
"""Score a structured reviewer response against a synthetic fixture's rubric.

Usage: python scripts/score_review.py evaluations/sample-review.json
The matching is explicit by expected finding ID; a human must still audit
whether submitted claims are actually supported by source code.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEVERITY = {"P0", "P1", "P2", "P3"}

def score(case: dict, review: dict) -> dict:
    expected = {item["id"]: item for item in case["expected"]}
    seen = set()
    points = 0
    details = []
    for finding in review.get("findings", []):
        fid = finding.get("id", "")
        if fid in expected and fid not in seen:
            seen.add(fid)
            gold = expected[fid]
            cause = bool(finding.get("trigger") and finding.get("invariant"))
            severity = finding.get("severity") == gold["severity"]
            fix = bool(finding.get("fix"))
            test = bool(finding.get("test"))
            gained = 2 * cause + int(severity) + int(fix) + int(test)
            points += gained
            details.append({"id": fid, "score": gained, "max": 5})
        else:
            penalty = finding.get("severity") in {"P0", "P1"}
            points -= int(penalty)
            details.append({"id": fid, "score": -int(penalty), "max": 0, "unmatched": True})
    return {"case_id": case["id"], "score": points, "max": 5 * len(expected), "missed": sorted(set(expected)-seen), "details": details, "caveat": "Self-reported finding IDs and nonempty fields are not proof of correctness. Human evidence review required."}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("review", type=Path)
    args = parser.parse_args()
    manifest = json.loads((ROOT / "evaluations" / "cases.json").read_text())
    review = json.loads(args.review.read_text())
    case = next((c for c in manifest["cases"] if c["id"] == review.get("case_id")), None)
    if case is None:
        parser.error("unknown case_id")
    print(json.dumps(score(case, review), indent=2))

if __name__ == "__main__":
    main()
