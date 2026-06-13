# Kubernetes Add-on Registry

Central registry of all supported Kubernetes addons, extensions, and operators.

## Structure

```
k8s-addon-registry/
├── addons/              # Addon definitions by category
│   ├── monitoring.yaml
│   ├── networking.yaml
│   ├── storage.yaml
│   ├── security.yaml
│   ├── service-mesh.yaml
│   └── autoscaling.yaml
├── manifests/           # Kubernetes manifests
│   ├── default-namespace.yaml
│   └── addon-rbac.yaml
├── schemas/             # Validation schemas
│   └── addon_schema.json
├── config/              # Registry configuration
│   └── registry-config.yaml
└── scripts/             # Utility scripts
    ├── validate.py
    └── list_addons.py
```

## Adding a New Addon

1. Determine the addon category (monitoring, networking, storage, security, service-mesh, autoscaling).
2. Add the addon entry to the appropriate YAML file under `addons/`.
3. Run `python scripts/validate.py` to verify.
4. Submit a PR for review.

## Related Repositories

- [cloud-service-catalog](../cloud-service-catalog) - Master service catalog
- [infra-templates](../infra-templates) - Templates using these addons
- [monitoring-service-registry](../monitoring-service-registry) - Monitoring configurations
