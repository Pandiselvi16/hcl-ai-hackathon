#!/usr/bin/env python3
"""Validate infrastructure templates."""

import os
import sys

try:
    import yaml
except ImportError:
    print("PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
TEMPLATE_DIRS = ["vm", "kubernetes", "storage", "network", "composite"]

REQUIRED_FIELDS = ["name", "description", "version", "category", "status"]


def validate_template(tmpl, filepath):
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in tmpl:
            errors.append(f"[{filepath}] Missing '{field}'")
    if tmpl.get("status") not in ["active", "deprecated", "draft"]:
        errors.append(f"[{filepath}] Invalid status '{tmpl.get('status')}'")
    return errors


def main():
    all_errors = []
    total = 0

    for dirname in TEMPLATE_DIRS:
        dirpath = os.path.join(BASE_DIR, dirname)
        if not os.path.isdir(dirpath):
            continue
        for filename in sorted(os.listdir(dirpath)):
            if not filename.endswith((".yaml", ".yml")):
                continue
            filepath = os.path.join(dirpath, filename)
            with open(filepath) as f:
                data = yaml.safe_load(f)
            tmpl = data.get("template", data)
            total += 1
            all_errors.extend(validate_template(tmpl, f"{dirname}/{filename}"))

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        sys.exit(1)
    else:
        print(f"All templates valid. Total: {total} templates.")
        sys.exit(0)


if __name__ == "__main__":
    main()
