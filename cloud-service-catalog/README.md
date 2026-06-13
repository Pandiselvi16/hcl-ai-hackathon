# Cloud Service Catalog

Master catalog of all cloud platform services. This is the central reference that links
to all specialized sub-catalogs.

## Structure

```
cloud-service-catalog/
├── compute/             # Compute services
│   └── compute-services.yaml
├── networking/          # Networking services
│   └── network-services.yaml
├── storage/             # Storage services
│   └── storage-services.yaml
├── security/            # Security services
│   └── security-services.yaml
├── ai/                  # AI/ML services
│   └── ai-services.yaml
├── analytics/           # Analytics services
│   └── analytics-services.yaml
├── devops/              # DevOps services
│   └── devops-services.yaml
├── services.yaml        # Master index
├── references/          # Cross-repo references
│   ├── repository-map.json
│   └── cross-repo-dependencies.json
├── schemas/
│   └── service_schema.json
└── scripts/
    ├── validate_service.py
    └── sync_catalogs.py
```

## Interconnected Repositories

```
cloud-service-catalog (this repo)
      │
      ├── cloud-vm-catalog
      ├── k8s-addon-registry
      ├── cloud-storage-catalog
      ├── cloud-regions
      ├── network-service-catalog
      ├── container-image-catalog
      ├── database-service-catalog
      ├── monitoring-service-registry
      ├── infra-templates
      ├── cloud-iam-policies
      └── cloud-backup-policies
```

## Multi-Repo Ticket Examples

| Ticket | Repositories Modified |
|--------|----------------------|
| Add VM type gp-large-v2 | cloud-vm-catalog, cloud-service-catalog |
| Enable gp-large-v2 in asia-south-2 | cloud-vm-catalog, cloud-regions |
| Add PostgreSQL 18 | database-service-catalog, cloud-service-catalog |
| Add vector-search service | cloud-service-catalog |
| Add latency alert for API | monitoring-service-registry |
