#!/usr/bin/env python3
"""Validate cloud service catalog entries."""

import os
import sys

try:
    import yaml
except ImportError:
    print("PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
SERVICE_DIRS = ["compute", "networking", "storage", "security", "ai", "analytics", "devops"]


def validate_service(service, filepath):
    errors = []
    if "name" not in service:
        errors.append(f"[{filepath}] Missing 'name'")
    if "description" not in service:
        errors.append(f"[{filepath}] Service '{service.get('name')}' missing 'description'")
    if "status" not in service:
        errors.append(f"[{filepath}] Service '{service.get('name')}' missing 'status'")
    return errors


def main():
    all_errors = []
    total = 0

    for dirname in SERVICE_DIRS:
        dirpath = os.path.join(BASE_DIR, dirname)
        if not os.path.isdir(dirpath):
            continue
        for filename in sorted(os.listdir(dirpath)):
            if not filename.endswith((".yaml", ".yml")):
                continue
            filepath = os.path.join(dirpath, filename)
            with open(filepath) as f:
                data = yaml.safe_load(f)
            for service in data.get("services", []):
                total += 1
                all_errors.extend(validate_service(service, f"{dirname}/{filename}"))

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        sys.exit(1)
    else:
        print(f"All services valid. Total: {total} services.")
        sys.exit(0)


if __name__ == "__main__":
    main()
