#!/usr/bin/env python3
"""Validate backup policy definitions."""

import os
import sys

try:
    import yaml
except ImportError:
    print("PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

POLICIES_DIR = os.path.join(os.path.dirname(__file__), "..", "policies")

REQUIRED_FIELDS = ["name", "description", "resource_type", "status"]


def validate_policy(policy, filename):
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in policy:
            errors.append(f"[{filename}] Policy '{policy.get('name', 'unknown')}': missing '{field}'")
    if "schedule" not in policy and "versioning" not in policy:
        errors.append(f"[{filename}] Policy '{policy.get('name')}': missing 'schedule' or 'versioning'")
    if policy.get("status") not in ["active", "deprecated", "draft"]:
        errors.append(f"[{filename}] Policy '{policy.get('name')}': invalid status")
    return errors


def main():
    all_errors = []
    total = 0

    for filename in sorted(os.listdir(POLICIES_DIR)):
        if not filename.endswith((".yaml", ".yml")):
            continue
        with open(os.path.join(POLICIES_DIR, filename)) as f:
            data = yaml.safe_load(f)
        for policy in data.get("policies", []):
            total += 1
            all_errors.extend(validate_policy(policy, filename))

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        sys.exit(1)
    else:
        print(f"All backup policies valid. Total: {total} policies.")
        sys.exit(0)


if __name__ == "__main__":
    main()
