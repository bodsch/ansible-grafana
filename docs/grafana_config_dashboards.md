# `grafana_config_dashboards`

```yaml
grafana_config_dashboards:
  # Number dashboard versions to keep (per dashboard). Default: 20, Minimum: 1
  versions_to_keep: 20
  # Minimum dashboard refresh interval. When set, this will restrict users to set the refresh interval of a dashboard lower than given interval. Per default this is 5 seconds.
  # The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.
  min_refresh_interval: 5s
  # Path to the default home dashboard. If this value is empty, then Grafana uses StaticRootPath + "dashboards/home.json"
  default_home_dashboard_path: ""
```
