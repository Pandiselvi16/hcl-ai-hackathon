#!/usr/bin/env python3
"""Validate IAM policy and role definitions."""

import os
import sys
import json

try:
    import yaml
except ImportError:
    print("PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")


def validate_roles():
    errors = []
    total = 0
    roles_dir = os.path.join(BASE_DIR, "roles")
    role_names = set()

    for filename in sorted(os.listdir(roles_dir)):
        if not filename.endswith((".yaml", ".yml")):
            continue
        with open(os.path.join(roles_dir, filename)) as f:
            data = yaml.safe_load(f)
        for role in data.get("roles", []):
            total += 1
            name = role.get("name")
            if not name:
                errors.append(f"[{filename}] Role missing 'name'")
                continue
            if name in role_names:
                errors.append(f"[{filename}] Duplicate role name: {name}")
            role_names.add(name)
            if "permissions" not in role:
                errors.append(f"[{filename}] Role '{name}' missing 'permissions'")
            if "status" not in role:
                errors.append(f"[{filename}] Role '{name}' missing 'status'")

    return errors, total


def validate_policies():
    errors = []
    total = 0
    policies_dir = os.path.join(BASE_DIR, "policies")

    for filename in sorted(os.listdir(policies_dir)):
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(policies_dir, filename)) as f:
            data = json.load(f)
        for policy in data.get("policies", []):
            total += 1
            if "name" not in policy:
                errors.append(f"[{filename}] Policy missing 'name'")
            if "status" not in policy:
                errors.append(f"[{filename}] Policy '{policy.get('name')}' missing 'status'")

    return errors, total


def main():
    role_errors, role_count = validate_roles()
    policy_errors, policy_count = validate_policies()
    all_errors = role_errors + policy_errors

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        sys.exit(1)
    else:
        print(f"All IAM definitions valid. Roles: {role_count}, Policies: {policy_count}")
        sys.exit(0)


if __name__ == "__main__":
    main()
