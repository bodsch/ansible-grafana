# `grafana_config_quota`

> Not implemented yet.
> Needs support!

```yaml
grafana_config_quota:
  enabled: false
  #### set quotas to -1 to make unlimited. ####
  # limit number of users per Org.
  org_user: 10
  # limit number of dashboards per Org.
  org_dashboard: 100
  # limit number of data_sources per Org.
  org_data_source: 10
  # limit number of api_keys per Org.
  org_api_key: 10
  # limit number of alerts per Org.
  org_alert_rule: 100
  # limit number of orgs a user can create.
  user_org: 10
  # Global limit of users.
  global_user: -1
  # global limit of orgs.
  global_org: -1
  # global limit of dashboards
  global_dashboard: -1
  # global limit of api_keys
  global_api_key: -1
  # global limit on number of logged in users.
  global_session: -1
  # global limit of alerts
  global_alert_rule: -1
```
