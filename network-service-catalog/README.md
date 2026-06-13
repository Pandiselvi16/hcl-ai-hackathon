# Network Service Catalog

Central registry of all network services: load balancers, gateways, firewalls, DNS, VPN, and VPC templates.

## Structure

```
network-service-catalog/
├── load-balancers/      # Load balancer definitions
│   ├── lb.yaml
│   └── lb-profiles.yaml
├── gateways/            # Network gateway services
│   └── gateways.yaml
├── firewalls/           # Firewall rules and security groups
│   ├── firewall_rules.json
│   └── security-groups.json
├── dns/                 # DNS zones and services
│   └── dns-zones.yaml
├── vpn/                 # VPN connectivity
│   └── vpn-connections.yaml
├── vpc/                 # VPC templates
│   └── vpc-templates.yaml
├── schemas/
│   └── network_schema.json
└── scripts/
    └── validate_network.py
```

## Related Repositories

- [cloud-regions](../cloud-regions) - Regions where services are available
- [cloud-service-catalog](../cloud-service-catalog) - Master service catalog
- [infra-templates](../infra-templates) - Infrastructure templates using network services
