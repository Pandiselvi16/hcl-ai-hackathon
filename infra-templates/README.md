# Infrastructure Templates

Reusable infrastructure-as-code templates for common deployment patterns.

## Structure

```
infra-templates/
├── vm/                  # VM templates
│   ├── vm-small.yaml
│   ├── vm-medium.yaml
│   ├── vm-large.yaml
│   └── vm-gpu.yaml
├── kubernetes/          # K8s cluster templates
│   ├── k8s-basic.yaml
│   └── k8s-production.yaml
├── storage/             # Storage templates
│   └── storage-basic.yaml
├── network/             # Network templates
│   ├── vpc-standard.yaml
│   └── vpc-advanced.yaml
├── composite/           # Multi-component templates
│   ├── web-app-stack.yaml
│   ├── data-pipeline.yaml
│   └── ml-platform.yaml
├── schemas/
│   └── template_schema.json
└── scripts/
    └── validate_template.py
```

## Related Repositories

- [cloud-vm-catalog](../cloud-vm-catalog) - Available VM instance types
- [k8s-addon-registry](../k8s-addon-registry) - Kubernetes addons
- [cloud-storage-catalog](../cloud-storage-catalog) - Storage tiers
- [network-service-catalog](../network-service-catalog) - Network services
- [database-service-catalog](../database-service-catalog) - Database engines
