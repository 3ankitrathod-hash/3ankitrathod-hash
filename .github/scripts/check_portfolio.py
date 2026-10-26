#!/usr/bin/env python3
"""Validate the profile repository's required project READMEs and local Markdown links."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
REQUIRED_READMES = [
    "README.md",
    "customer-feedback-analysis/README.md",
    "employee-wellness-eda/README.md",
    "global-social-media-analytics/README.md",
    "global-trade-data-analysis/README.md",
    "healthcare-analytics-sql/README.md",
    "olympic-athlete-analysis/README.md",
    "space-mission-analysis/README.md",
    "supply-chain-inventory-analytics/README.md",
]
LINK_PATTERN = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")

errors = []
for relative in REQUIRED_READMES:
    if not (ROOT / relative).is_file():
        errors.append(f"Missing required README: {relative}")

readmes = sorted(ROOT.rglob("README.md"))
checked_links = 0
for readme in readmes:
    try:
        content = readme.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"Cannot read {readme.relative_to(ROOT)}: {exc}")
        continue

    for raw_target in LINK_PATTERN.findall(content):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        parsed = urlsplit(target)
        if not target or parsed.scheme or parsed.netloc or target.startswith("#"):
            continue
        path_text = unquote(parsed.path)
        if not path_text:
            continue
        destination = (readme.parent / path_text).resolve()
        checked_links += 1
        if not destination.exists():
            errors.append(
                f"Broken local link in {readme.relative_to(ROOT)}: {target}"
            )

if errors:
    print("Portfolio integrity check failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Portfolio integrity check passed: {len(readmes)} README files and {checked_links} local links checked.")
