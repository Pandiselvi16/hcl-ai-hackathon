#!/usr/bin/env python3
"""List all database services and versions."""

import json
import os

RELATIONAL_DIR = os.path.join(os.path.dirname(__file__), "..", "relational")
NOSQL_DIR = os.path.join(os.path.dirname(__file__), "..", "nosql")


def list_dir(dirpath, category):
    entries = []
    if not os.path.isdir(dirpath):
        return entries
    for filename in sorted(os.listdir(dirpath)):
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(dirpath, filename)) as f:
            data = json.load(f)
        engine = data.get("engine", "unknown")
        for ver in data.get("versions", []):
            entries.append({
                "category": category,
                "engine": engine,
                "version": ver["version"],
                "status": ver.get("status", "unknown"),
            })
    return entries


def main():
    all_entries = list_dir(RELATIONAL_DIR, "relational") + list_dir(NOSQL_DIR, "nosql")
    print(f"{'Engine':<15} {'Version':<10} {'Category':<12} {'Status':<10}")
    print("-" * 47)
    for e in all_entries:
        print(f"{e['engine']:<15} {e['version']:<10} {e['category']:<12} {e['status']:<10}")
    print(f"\nTotal: {len(all_entries)} database versions")


if __name__ == "__main__":
    main()
