#!/usr/bin/env python3
"""Validate container image catalog entries."""

import os
import sys

try:
    import yaml
except ImportError:
    print("PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "images")

REQUIRED_FIELDS = ["name", "registry", "repository", "tag", "os", "architecture", "status"]


def validate_image(image, filename):
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in image:
            errors.append(f"[{filename}] Image '{image.get('name', 'unknown')}': missing '{field}'")
    if image.get("status") not in ["active", "deprecated", "preview"]:
        errors.append(f"[{filename}] Image '{image.get('name')}': invalid status")
    return errors


def main():
    all_errors = []
    total = 0

    for filename in sorted(os.listdir(IMAGES_DIR)):
        if not filename.endswith((".yaml", ".yml")):
            continue
        with open(os.path.join(IMAGES_DIR, filename)) as f:
            data = yaml.safe_load(f)
        for image in data.get("images", []):
            total += 1
            all_errors.extend(validate_image(image, filename))

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}")
        sys.exit(1)
    else:
        print(f"All image definitions valid. Total: {total} images.")
        sys.exit(0)


if __name__ == "__main__":
    main()
