# `grafana_config_live`

> Not implemented yet.
> Needs support!

```yaml
grafana_config_live:
  # max_connections to Grafana Live WebSocket endpoint per Grafana server instance. See Grafana Live docs
  # if you are planning to make it higher than default 100 since this can require some OS and infrastructure
  # tuning. 0 disables Live, -1 means unlimited connections.
  max_connections: 100
  # allowed_origins is a comma-separated list of origins that can establish connection with Grafana Live.
  # If not set then origin will be matched over root_url. Supports wildcard symbol "*".
  allowed_origins: ""
  # engine defines an HA (high availability) engine to use for Grafana Live. By default no engine used - in
  # this case Live features work only on a single Grafana server. Available options: "redis".
  # Setting ha_engine is an EXPERIMENTAL feature.
  ha_engine: ""
  # ha_engine_address sets a connection address for Live HA engine. Depending on engine type address format can differ.
  # For now we only support Redis connection address in "host:port" format.
  # This option is EXPERIMENTAL.
  ha_engine_address: "127.0.0.1:6379"
```
