# Cloud Regions

Central registry of all cloud regions, availability zones, and edge locations.

## Structure

```
cloud-regions/
├── regions/             # Region definitions by geography
│   ├── us.json
│   ├── europe.json
│   ├── asia.json
│   ├── south-america.json
│   ├── africa.json
│   └── middle-east.json
├── zones/
│   └── edge-locations.json
├── latency/
│   └── inter-region-latency.json
├── compliance/
│   └── data-residency.yaml
├── schemas/
│   └── region_schema.json
└── scripts/
    ├── validate_regions.py
    └── list_regions.py
```

## Adding a New Region

1. Find the appropriate geography file under `regions/`.
2. Add the region with all required fields (name, display_name, AZs, services, compliance).
3. Run `python scripts/validate_regions.py` to verify.
4. Submit a PR for review.

## Related Repositories

- [cloud-vm-catalog](../cloud-vm-catalog) - Instance types available per region
- [cloud-storage-catalog](../cloud-storage-catalog) - Storage tiers per region
- [cloud-service-catalog](../cloud-service-catalog) - Master service catalog
