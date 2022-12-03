# `grafana_datasources`

Supported datasource types are:

- prometheus
- loki
- graphite
- influxdb

```yaml
grafana_datasources:
  prometheus:
    state: present
    datasource:
      type: "prometheus"
      # access: "proxy"
      url: "http://prometheus.mydomain"
    # basic_auth:
    #   # Auth: true
    #   username: "admin"
    #   password: "password"
    default: true
    # json_data:
    #   tlsAuth: false
    #   tlsAuthWithCACert: false
    #   tlsSkipVerify: true

  loki:
    datasource:
      type: "loki"
      url: "http://loki.mydomain"
    editable: true
```
