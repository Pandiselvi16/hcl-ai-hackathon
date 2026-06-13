# Container Image Catalog

Approved container images for the cloud platform, including base OS, language runtimes, and ML images.

## Structure

```
container-image-catalog/
├── images/              # Image definitions
│   ├── base-images.yaml
│   ├── runtime-images.yaml
│   └── ml-images.yaml
├── registries/          # Approved registries
│   └── approved-registries.json
├── policies/            # Image policies
│   ├── image-policies.yaml
│   └── vulnerability-thresholds.yaml
├── scanning/            # Scan configuration
│   └── scan-config.yaml
├── schemas/
│   └── image_schema.json
└── scripts/
    └── validate_images.py
```

## Related Repositories

- [k8s-addon-registry](../k8s-addon-registry) - Kubernetes addons
- [cloud-service-catalog](../cloud-service-catalog) - Master service catalog
