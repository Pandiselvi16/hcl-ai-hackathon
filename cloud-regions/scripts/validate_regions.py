#!/usr/bin/env python3
"""Validate cloud region definitions."""

import json
import os
import sys

REGIONS_DIR = os.path.join(os.path.dirname(__file__), "..", "regions")

REQUIRED_FIELDS = ["name", "display_name", "availability_zones", "status", "services"]


def validate_region(region, filename):
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in region:
            errors.append(f"[{filename}] Region '{region.get('name', 'unknown')}': missing '{field}'")
    if region.get("status") not in ["active", "deprecated", "coming-soon"]:
        errors.append(f"[{filename}] Region '{region.get('name')}': invalid status")
    azs = region.get("availability_zones", [])
    if len(azs) < 1:
        errors.append(f"[{filename}] Region '{region.get('name')}': must have at least 1 AZ")
    return errors


def main():
    all_errors = []
    total = 0
    region_names = set()

    for filename in sorted(os.listdir(REGIONS_DIR)):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(REGIONS_DIR, filename)
        with open(filepath) as f:
            data = json.load(f)
        for region in data.get("regions", []):
            total += 1
            name = region.get("name")
            if name in region_names:
                all_errors.append(f"Duplicate region: {name}")
            region_names.add(name)
            all_errors.extend(validate_region(region, filename))

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        sys.exit(1)
    else:
        print(f"All region definitions valid. Total: {total} regions.")
        sys.exit(0)


if __name__ == "__main__":
    main()
