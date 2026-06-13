# Monitoring Service Registry

Central registry for monitoring, logging, alerting, and observability configurations.

## Structure

```
monitoring-service-registry/
├── metrics/             # Metrics configuration
│   ├── prometheus.yaml
│   ├── custom-metrics.yaml
│   └── slo-definitions.yaml
├── logs/                # Logging configuration
│   ├── logging.yaml
│   └── log-pipelines.yaml
├── alerts/              # Alert rules and notifications
│   ├── alert-rules.yaml
│   └── notification-channels.yaml
├── dashboards/          # Dashboard definitions
│   └── default-dashboards.yaml
├── integrations/        # Third-party integrations
│   └── integrations.yaml
├── schemas/
│   └── monitoring_schema.json
└── scripts/
    └── validate_monitoring.py
```

## Related Repositories

- [k8s-addon-registry](../k8s-addon-registry) - Monitoring addons (Prometheus, Grafana)
- [cloud-service-catalog](../cloud-service-catalog) - Master service catalog
