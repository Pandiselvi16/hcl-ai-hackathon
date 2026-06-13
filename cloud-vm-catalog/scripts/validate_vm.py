#!/usr/bin/env python3
"""Validate VM instance definitions against the schema."""

import json
import os
import sys


SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "..", "schemas", "vm_schema.json")
INSTANCES_DIR = os.path.join(os.path.dirname(__file__), "..", "instances")


def load_json(path):
    with open(path) as f:
        return json.load(f)


def validate_instance(instance, schema):
    errors = []
    for field in schema.get("required", []):
        if field not in instance:
            errors.append(f"Missing required field: {field}")

    props = schema.get("properties", {})
    for key, value in instance.items():
        if key in props:
            expected_type = props[key].get("type")
            if expected_type == "string" and not isinstance(value, str):
                errors.append(f"Field '{key}' should be string, got {type(value).__name__}")
            elif expected_type == "integer" and not isinstance(value, int):
                errors.append(f"Field '{key}' should be integer, got {type(value).__name__}")
            elif expected_type == "number" and not isinstance(value, (int, float)):
                errors.append(f"Field '{key}' should be number, got {type(value).__name__}")
            elif expected_type == "array" and not isinstance(value, list):
                errors.append(f"Field '{key}' should be array, got {type(value).__name__}")
    return errors


def main():
    schema = load_json(SCHEMA_PATH)
    all_errors = []

    for filename in os.listdir(INSTANCES_DIR):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(INSTANCES_DIR, filename)
        data = load_json(filepath)
        for instance in data.get("instances", []):
            errs = validate_instance(instance, schema)
            if errs:
                all_errors.append((filename, instance.get("name", "unknown"), errs))

    if all_errors:
        for filename, name, errs in all_errors:
            for err in errs:
                print(f"ERROR [{filename}] {name}: {err}")
        sys.exit(1)
    else:
        print("All VM instance definitions are valid.")
        sys.exit(0)


if __name__ == "__main__":
    main()
