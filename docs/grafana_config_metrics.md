# `grafana_config_metrics`

```yaml
grafana_config_metrics:
  # Metrics available at HTTP URL /metrics and /metrics/plugins/:pluginId
  # Disable / Enable internal metrics
  enabled: false
  # Graphite Publish interval
  interval_seconds: 10
  # Disable total stats (stat_totals_*) metrics to be generated
  disable_total_stats: false
  # If both are set, basic auth will be required for the metrics endpoints.
  basic_auth_username: ""
  basic_auth_password: ""
  # Metrics environment info adds dimensions to the `grafana_environment_info` metric, which
  # can expose more information about the Grafana instance.
  environment_info: {}
  #  exampleLabel1: exampleValue1
  #  exampleLabel2: exampleValue2
  # Send internal metrics to Graphite
  graphite:
    # Enable by setting the address setting (ex localhost:2003)
    address: ""
    prefix: prod.grafana.%(instance_name)s.
```
