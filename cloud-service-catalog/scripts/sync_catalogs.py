#!/usr/bin/env python3
"""Check that the master catalog references match sub-catalogs."""

import json
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
REPO_MAP_PATH = os.path.join(BASE_DIR, "references", "repository-map.json")


def main():
    with open(REPO_MAP_PATH) as f:
        repo_map = json.load(f)

    print("Repository Map Verification")
    print("=" * 50)
    for repo in repo_map.get("repositories", []):
        repo_path = os.path.join(BASE_DIR, "..", repo["url"])
        exists = os.path.isdir(repo_path)
        status = "FOUND" if exists else "MISSING"
        print(f"  {repo['name']:<30} [{status}]")

    print(f"\nTotal repositories: {len(repo_map.get('repositories', []))}")


if __name__ == "__main__":
    main()
