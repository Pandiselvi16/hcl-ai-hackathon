#!/usr/bin/env python3
"""Validate monitoring configurations."""

import os
import sys

try:
    import yaml
except ImportError:
    print("PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")


def validate_alerts():
    errors = []
    filepath = os.path.join(BASE_DIR, "alerts", "alert-rules.yaml")
    with open(filepath) as f:
        data = yaml.safe_load(f)
    for rule in data.get("alert_rules", []):
        if "name" not in rule:
            errors.append("Alert rule missing 'name'")
        if "severity" not in rule:
            errors.append(f"Alert '{rule.get('name')}' missing 'severity'")
        elif rule["severity"] not in ["info", "warning", "critical"]:
            errors.append(f"Alert '{rule['name']}' has invalid severity '{rule['severity']}'")
        if "expression" not in rule:
            errors.append(f"Alert '{rule.get('name')}' missing 'expression'")
    return errors, len(data.get("alert_rules", []))


def main():
    all_errors, total = validate_alerts()

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        sys.exit(1)
    else:
        print(f"All monitoring configurations valid. Alert rules: {total}")
        sys.exit(0)


if __name__ == "__main__":
    main()
