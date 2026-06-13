# Cloud Storage Catalog

Central registry of all storage classes, tiers, and policies.

## Structure

```
cloud-storage-catalog/
├── storage/             # Storage tier definitions
│   ├── block-storage.json
│   ├── object-storage.json
│   ├── file-storage.json
│   └── archive-storage.json
├── policies/            # Storage policies
│   ├── replication-policies.yaml
│   └── lifecycle-policies.yaml
├── schemas/
│   └── storage_schema.json
├── config/
│   └── storage-defaults.json
└── scripts/
    ├── validate_storage.py
    └── calculate_cost.py
```

## Adding a New Storage Tier

1. Choose the appropriate category file under `storage/`.
2. Add the tier definition with all required fields.
3. Run `python scripts/validate_storage.py` to verify.
4. Submit a PR for review.

## Related Repositories

- [cloud-vm-catalog](../cloud-vm-catalog) - VM instances that use these storage tiers
- [cloud-regions](../cloud-regions) - Regions where storage is available
- [cloud-backup-policies](../cloud-backup-policies) - Backup policies for storage
