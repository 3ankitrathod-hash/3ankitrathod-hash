#!/usr/bin/env python3
"""Check that every Jupyter notebook is valid JSON and every code cell is valid Python.

Uses only the standard library, so it needs no extra dependencies in CI.
"""

import ast
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAGIC_PREFIXES = ("%", "!")  # IPython magics and shell escapes are not plain Python

errors = []
notebook_count = 0
code_cell_count = 0

for notebook in sorted(ROOT.rglob("*.ipynb")):
    if ".ipynb_checkpoints" in notebook.parts:
        continue
    name = notebook.relative_to(ROOT)

    try:
        data = json.loads(notebook.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{name}: cannot read as JSON: {exc}")
        continue

    if not isinstance(data, dict) or "nbformat" not in data or not isinstance(data.get("cells"), list):
        errors.append(f"{name}: not a valid notebook (missing 'nbformat' or 'cells')")
        continue

    notebook_count += 1
    for number, cell in enumerate(data["cells"], start=1):
        if cell.get("cell_type") != "code":
            continue
        code_cell_count += 1
        source = cell.get("source", "")
        if isinstance(source, list):
            source = "".join(source)
        lines = ["" if line.lstrip().startswith(MAGIC_PREFIXES) else line for line in source.splitlines()]
        try:
            ast.parse("\n".join(lines))
        except SyntaxError as exc:
            errors.append(f"{name}: code cell {number}: {exc.msg} (line {exc.lineno})")

if notebook_count == 0:
    errors.append("No notebooks found; expected at least one .ipynb file.")

if errors:
    print("Notebook check failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Notebook check passed: {notebook_count} notebooks, {code_cell_count} code cells parsed.")
