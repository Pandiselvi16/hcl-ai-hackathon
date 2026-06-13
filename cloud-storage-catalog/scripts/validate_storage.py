#!/usr/bin/env python3
"""Validate storage tier definitions."""

import json
import os
import sys

STORAGE_DIR = os.path.join(os.path.dirname(__file__), "..", "storage")

REQUIRED_FIELDS = ["name", "status"]


def validate_tier(tier, filename):
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in tier:
            errors.append(f"[{filename}] Tier '{tier.get('name', 'unknown')}': missing '{field}'")
    if tier.get("status") not in ["active", "deprecated", "preview"]:
        errors.append(f"[{filename}] Tier '{tier.get('name')}': invalid status")
    price = tier.get("price_per_gb_month_usd")
    if price is not None and price < 0:
        errors.append(f"[{filename}] Tier '{tier.get('name')}': negative price")
    return errors


def main():
    all_errors = []
    total = 0
    for filename in sorted(os.listdir(STORAGE_DIR)):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(STORAGE_DIR, filename)
        with open(filepath) as f:
            data = json.load(f)
        for tier in data.get("tiers", []):
            total += 1
            all_errors.extend(validate_tier(tier, filename))

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        sys.exit(1)
    else:
        print(f"All storage definitions valid. Total: {total} tiers.")
        sys.exit(0)


if __name__ == "__main__":
    main()
