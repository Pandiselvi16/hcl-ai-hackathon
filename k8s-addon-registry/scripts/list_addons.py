#!/usr/bin/env python3
"""List all registered Kubernetes addons."""

import os

try:
    import yaml
except ImportError:
    print("PyYAML required. Install with: pip install pyyaml")
    exit(1)

ADDONS_DIR = os.path.join(os.path.dirname(__file__), "..", "addons")


def main():
    addons = []
    for filename in sorted(os.listdir(ADDONS_DIR)):
        if not filename.endswith((".yaml", ".yml")):
            continue
        with open(os.path.join(ADDONS_DIR, filename)) as f:
            data = yaml.safe_load(f)
        category = data.get("category", "unknown")
        for addon in data.get("addons", []):
            addons.append({
                "category": category,
                "name": addon["name"],
                "version": addon["version"],
                "status": addon["status"],
            })

    print(f"{'Name':<25} {'Category':<15} {'Version':<12} {'Status':<10}")
    print("-" * 62)
    for a in addons:
        print(f"{a['name']:<25} {a['category']:<15} {a['version']:<12} {a['status']:<10}")
    print(f"\nTotal: {len(addons)} addons")


if __name__ == "__main__":
    main()
