# Cloud Backup Policies

Backup, disaster recovery, and data retention policies for all cloud resources.

## Structure

```
cloud-backup-policies/
├── policies/            # Backup policies by resource type
│   ├── vm-backup-policies.yaml
│   ├── database-backup-policies.yaml
│   ├── storage-backup-policies.yaml
│   └── k8s-backup-policies.yaml
├── disaster-recovery/   # DR plans and runbooks
│   ├── dr-plans.yaml
│   └── runbooks.yaml
├── compliance/          # Retention requirements
│   └── retention-requirements.yaml
├── schemas/
│   └── backup_schema.json
└── scripts/
    └── validate_backup.py
```

## Related Repositories

- [cloud-vm-catalog](../cloud-vm-catalog) - VMs that need backups
- [database-service-catalog](../database-service-catalog) - Databases that need backups
- [cloud-storage-catalog](../cloud-storage-catalog) - Storage for backups
- [cloud-regions](../cloud-regions) - Regions for cross-region DR
- [cloud-service-catalog](../cloud-service-catalog) - Master service catalog
