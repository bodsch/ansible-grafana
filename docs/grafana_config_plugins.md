# `grafana_config_plugins`

> Not implemented yet.
> Needs support!

```yaml
grafana_config_plugins:
  enable_alpha: false
  app_tls_skip_verify_insecure: false
  # Enter a comma-separated list of plugin identifiers to identify plugins to load even if they are unsigned.
  # Plugins with modified signatures are never loaded.
  allow_loading_unsigned_plugins: []
  # Enable or disable installing / uninstalling / updating plugins directly from within Grafana.
  plugin_admin_enabled: false
  plugin_admin_external_manage_enabled: false
  plugin_catalog_url: https://grafana.com/grafana/plugins/
  # Enter a comma-separated list of plugin identifiers to hide in the plugin catalog.
  plugin_catalog_hidden_plugins: ""
```
