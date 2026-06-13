# Database Service Catalog

Managed database offerings including relational and NoSQL databases.

## Structure

```
database-service-catalog/
├── relational/          # Relational database engines
│   ├── postgres.json
│   ├── mysql.json
│   └── mariadb.json
├── nosql/               # NoSQL database engines
│   ├── documentdb.json
│   ├── redis.json
│   ├── cassandra.json
│   └── dynamodb.json
├── configs/             # Connection profiles
│   └── connection-profiles.yaml
├── schemas/
│   └── database_schema.json
└── scripts/
    ├── validate_db.py
    └── list_databases.py
```

## Related Repositories

- [cloud-vm-catalog](../cloud-vm-catalog) - VM instances for self-managed databases
- [cloud-storage-catalog](../cloud-storage-catalog) - Storage tiers for database volumes
- [cloud-backup-policies](../cloud-backup-policies) - Backup policies for databases
- [cloud-service-catalog](../cloud-service-catalog) - Master service catalog
