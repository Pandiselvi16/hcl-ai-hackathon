# Cloud VM Catalog

Central registry of all supported virtual machine instance types across the cloud platform.

## Structure

```
cloud-vm-catalog/
├── instances/           # VM instance type definitions
│   ├── general-purpose.json
│   ├── compute-optimized.json
│   ├── memory-optimized.json
│   ├── gpu-instances.json
│   ├── arm-instances.json
│   └── high-storage.json
├── pricing/             # Pricing models
│   ├── on-demand.json
│   ├── reserved.json
│   └── spot.json
├── schemas/             # JSON schemas for validation
│   └── vm_schema.json
├── config/              # Configuration and metadata
│   ├── instance-families.json
│   └── supported-regions.json
└── scripts/             # Utility scripts
    ├── validate_vm.py
    └── list_instances.py
```

## Adding a New Instance Type

1. Identify the appropriate category file under `instances/`.
2. Add the new instance definition following the schema in `schemas/vm_schema.json`.
3. Update pricing files under `pricing/` if applicable.
4. Run `python scripts/validate_vm.py` to verify.
5. Submit a PR for review.

## Related Repositories

- [cloud-regions](../cloud-regions) - Region and availability zone definitions
- [cloud-service-catalog](../cloud-service-catalog) - Master service catalog
- [infra-templates](../infra-templates) - Infrastructure templates using these instance types
