# Cloud IAM Policies

Identity and Access Management roles, policies, and service account configurations.

## Structure

```
cloud-iam-policies/
├── roles/               # IAM role definitions
│   ├── predefined-roles.yaml
│   └── custom-roles.yaml
├── policies/            # Access policies
│   ├── access-policies.json
│   └── resource-policies.json
├── service-accounts/    # Service account configurations
│   └── service-accounts.yaml
├── compliance/          # Audit and compliance config
│   └── audit-config.yaml
├── schemas/
│   └── iam_schema.json
└── scripts/
    └── validate_iam.py
```

## Related Repositories

- [cloud-service-catalog](../cloud-service-catalog) - Master service catalog (IAM as a service)
- [cloud-backup-policies](../cloud-backup-policies) - Backup access controls
- [monitoring-service-registry](../monitoring-service-registry) - Monitoring access
