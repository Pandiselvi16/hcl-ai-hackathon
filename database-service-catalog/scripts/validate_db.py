#!/usr/bin/env python3
"""Validate database service catalog entries."""

import json
import os
import sys

RELATIONAL_DIR = os.path.join(os.path.dirname(__file__), "..", "relational")
NOSQL_DIR = os.path.join(os.path.dirname(__file__), "..", "nosql")

REQUIRED_FIELDS = ["engine", "description"]


def validate_db(data, filename):
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"[{filename}] Missing '{field}'")
    for ver in data.get("versions", []):
        if "version" not in ver:
            errors.append(f"[{filename}] Version entry missing 'version' field")
        if "status" not in ver:
            errors.append(f"[{filename}] Version '{ver.get('version')}' missing 'status'")
    return errors


def scan_dir(dirpath):
    errors = []
    count = 0
    if not os.path.isdir(dirpath):
        return errors, count
    for filename in sorted(os.listdir(dirpath)):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(dirpath, filename)
        with open(filepath) as f:
            data = json.load(f)
        count += 1
        errors.extend(validate_db(data, filename))
    return errors, count


def main():
    all_errors = []
    total = 0
    for d in [RELATIONAL_DIR, NOSQL_DIR]:
        errs, cnt = scan_dir(d)
        all_errors.extend(errs)
        total += cnt

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        sys.exit(1)
    else:
        print(f"All database definitions valid. Total: {total} engines.")
        sys.exit(0)


if __name__ == "__main__":
    main()
