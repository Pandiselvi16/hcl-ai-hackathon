#!/usr/bin/env python3
"""Validate Kubernetes addon definitions."""

import os
import sys
import json

try:
    import yaml
except ImportError:
    print("PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

ADDONS_DIR = os.path.join(os.path.dirname(__file__), "..", "addons")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "..", "schemas", "addon_schema.json")

REQUIRED_FIELDS = ["name", "version", "description", "namespace", "helm_chart", "status", "supported_k8s_versions"]


def load_schema():
    with open(SCHEMA_PATH) as f:
        return json.load(f)


def validate_addon(addon, filename):
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in addon:
            errors.append(f"[{filename}] Addon '{addon.get('name', 'unknown')}': missing field '{field}'")

    if addon.get("status") not in ["active", "deprecated", "preview", "beta"]:
        errors.append(f"[{filename}] Addon '{addon.get('name')}': invalid status '{addon.get('status')}'")

    return errors


def main():
    all_errors = []
    addon_names = set()

    for filename in sorted(os.listdir(ADDONS_DIR)):
        if not filename.endswith((".yaml", ".yml")):
            continue
        filepath = os.path.join(ADDONS_DIR, filename)
        with open(filepath) as f:
            data = yaml.safe_load(f)

        for addon in data.get("addons", []):
            name = addon.get("name")
            if name in addon_names:
                all_errors.append(f"[{filename}] Duplicate addon name: {name}")
            addon_names.add(name)
            all_errors.extend(validate_addon(addon, filename))

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        sys.exit(1)
    else:
        print(f"All addons valid. Total: {len(addon_names)} addons.")
        sys.exit(0)


if __name__ == "__main__":
    main()
