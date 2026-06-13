#!/usr/bin/env python3
"""List all VM instance types across all categories."""

import json
import os

INSTANCES_DIR = os.path.join(os.path.dirname(__file__), "..", "instances")


def main():
    all_instances = []
    for filename in sorted(os.listdir(INSTANCES_DIR)):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(INSTANCES_DIR, filename)
        with open(filepath) as f:
            data = json.load(f)
        category = data.get("category", "unknown")
        for inst in data.get("instances", []):
            all_instances.append({
                "category": category,
                "name": inst["name"],
                "vcpus": inst["vcpus"],
                "memory_gb": inst["memory_gb"],
                "status": inst["status"],
            })

    print(f"{'Name':<20} {'Category':<20} {'vCPUs':<8} {'Memory (GB)':<12} {'Status':<10}")
    print("-" * 70)
    for inst in all_instances:
        print(f"{inst['name']:<20} {inst['category']:<20} {inst['vcpus']:<8} {inst['memory_gb']:<12} {inst['status']:<10}")
    print(f"\nTotal: {len(all_instances)} instance types")


if __name__ == "__main__":
    main()
