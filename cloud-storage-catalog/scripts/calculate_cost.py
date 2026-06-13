#!/usr/bin/env python3
"""Calculate monthly storage costs for given configurations."""

import json
import os
import sys

STORAGE_DIR = os.path.join(os.path.dirname(__file__), "..", "storage")


def load_tiers():
    tiers = {}
    for filename in os.listdir(STORAGE_DIR):
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(STORAGE_DIR, filename)) as f:
            data = json.load(f)
        for tier in data.get("tiers", []):
            tiers[tier["name"]] = tier
    return tiers


def calculate(tier_name, size_gb, tiers):
    tier = tiers.get(tier_name)
    if not tier:
        print(f"Unknown tier: {tier_name}")
        return None
    price = tier.get("price_per_gb_month_usd", 0)
    return round(price * size_gb, 2)


def main():
    if len(sys.argv) != 3:
        print("Usage: calculate_cost.py <tier_name> <size_gb>")
        sys.exit(1)

    tier_name = sys.argv[1]
    size_gb = int(sys.argv[2])
    tiers = load_tiers()
    cost = calculate(tier_name, size_gb, tiers)
    if cost is not None:
        print(f"Monthly cost for {size_gb}GB of {tier_name}: ${cost}")


if __name__ == "__main__":
    main()
