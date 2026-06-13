#!/usr/bin/env python3
"""Validate network service definitions."""

import json
import os
import sys

try:
    import yaml
except ImportError:
    print("PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
DIRS_TO_CHECK = ["load-balancers", "gateways", "dns", "vpn", "vpc"]


def validate_service(service, source):
    errors = []
    if "name" not in service:
        errors.append(f"[{source}] Missing 'name' field")
    if "status" not in service:
        errors.append(f"[{source}] Service '{service.get('name', 'unknown')}': missing 'status'")
    return errors


def main():
    all_errors = []
    total = 0

    for dirname in DIRS_TO_CHECK:
        dirpath = os.path.join(BASE_DIR, dirname)
        if not os.path.isdir(dirpath):
            continue
        for filename in sorted(os.listdir(dirpath)):
            filepath = os.path.join(dirpath, filename)
            if filename.endswith(".json"):
                with open(filepath) as f:
                    data = json.load(f)
                items = data.get("services", data.get("rule_templates", data.get("security_groups", [])))
            elif filename.endswith((".yaml", ".yml")):
                with open(filepath) as f:
                    data = yaml.safe_load(f)
                items = data.get("services", data.get("zones", data.get("vpc_templates", data.get("profiles", []))))
            else:
                continue

            for item in (items or []):
                total += 1
                all_errors.extend(validate_service(item, f"{dirname}/{filename}"))

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        sys.exit(1)
    else:
        print(f"All network service definitions valid. Total: {total} entries.")
        sys.exit(0)


if __name__ == "__main__":
    main()
