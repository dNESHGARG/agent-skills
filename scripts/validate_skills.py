#!/usr/bin/env python3
"""Validate skill metadata and basic structure without external dependencies."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "skills"
NAME = re.compile(r"^[a-z][a-z0-9-]*$")


def validate(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        return [f"{path}: missing opening YAML frontmatter"]
    metadata = parts[1]
    fields = {}
    for line in metadata.strip().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    name = fields.get("name", "")
    if not NAME.fullmatch(name):
        errors.append(f"{path}: invalid or missing name")
    if name != path.parent.name:
        errors.append(f"{path}: name does not match directory")
    if len(fields.get("description", "")) < 30:
        errors.append(f"{path}: description must be at least 30 characters")
    body = parts[2].strip()
    if len(body) < 500:
        errors.append(f"{path}: body too short to be operational")
    if not body.startswith("# "):
        errors.append(f"{path}: body must begin with an H1")
    return errors


def main() -> int:
    paths = sorted(ROOT.glob("*/SKILL.md"))
    if not paths:
        print("No skills found", file=sys.stderr)
        return 1
    errors = [error for path in paths for error in validate(path)]
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Validated {len(paths)} skill(s); {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
