#!/usr/bin/env python3
"""List all cloud regions and availability zones."""

import json
import os

REGIONS_DIR = os.path.join(os.path.dirname(__file__), "..", "regions")


def main():
    all_regions = []
    for filename in sorted(os.listdir(REGIONS_DIR)):
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(REGIONS_DIR, filename)) as f:
            data = json.load(f)
        continent = data.get("continent", "Unknown")
        for region in data.get("regions", []):
            all_regions.append({
                "continent": continent,
                "name": region["name"],
                "display_name": region["display_name"],
                "azs": len(region["availability_zones"]),
                "services": len(region.get("services", [])),
                "status": region["status"],
            })

    print(f"{'Region':<18} {'Display Name':<30} {'Continent':<18} {'AZs':<5} {'Services':<10} {'Status':<10}")
    print("-" * 91)
    for r in all_regions:
        print(f"{r['name']:<18} {r['display_name']:<30} {r['continent']:<18} {r['azs']:<5} {r['services']:<10} {r['status']:<10}")
    print(f"\nTotal: {len(all_regions)} regions")


if __name__ == "__main__":
    main()
