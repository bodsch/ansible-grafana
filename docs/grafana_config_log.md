# `grafana_config_log`

```yaml
grafana_config_log:
  # Either "console", "file", "syslog". Default is console and  file
  # Use space to separate multiple modes, e.g. "console file"
  mode:
    - console
    - file
  # Either "debug", "info", "warn", "error", "critical", default is "info"
  level: info
  # optional settings to set different levels for specific loggers. Ex filters: sqlstore:debug
  filters: []
  # For "console" mode only
  console:
    level: ""
    # log line format, valid options are text, console and json
    format: console
  # For "file" mode only
  file:
    level: ""
    # log line format, valid options are text, console and json
    format: text
    # This enables automated log rotate(switch of following options), default is true
    log_rotate: true
    # Max line number of single file, default is 1000000
    max_lines: 1000000
    # Max size shift of single file, default is 28 means 1 << 28, 256MB
    max_size_shift: 28
    # Segment log daily, default is true
    daily_rotate: true
    # Expired days of log file(delete after max days), default is 7
    max_days: 7
  syslog:
    level: ""
    # log line format, valid options are text, console and json
    format: text
    # Syslog network type and address. This can be udp, tcp, or unix. If left blank, the default unix endpoints will be used.
    network: ""
    address: ""
    # Syslog facility. user, daemon and local0 through local7 are valid.
    facility: ""
    # Syslog tag. By default, the process' argv[0] is used.
    tag: ""

  frontend:
    # Should Sentry javascript agent be initialized
    enabled: false
    # Defines which provider to use, default is Sentry
    provider: sentry
    # Sentry DSN if you want to send events to Sentry.
    sentry_dsn: ""
    # Custom HTTP endpoint to send events captured by the Sentry agent to. Default will log the events to stdout.
    custom_endpoint: /log
    # Rate of events to be reported between 0 (none) and 1 (all), float
    sample_rate: 1.0
    # Requests per second limit enforced an extended period, for Grafana backend log ingestion endpoint (/log).
    log_endpoint_requests_per_second_limit: 3
    # Max requests accepted per short interval of time for Grafana backend log ingestion endpoint (/log).
    log_endpoint_burst_limit: 15
    # Should error instrumentation be enabled, only affects Grafana Javascript Agent
    instrumentations_errors_enabled: true
    # Should console instrumentation be enabled, only affects Grafana Javascript Agent
    instrumentations_console_enabled: false
    # Should webvitals instrumentation be enabled, only affects Grafana Javascript Agent
    instrumentations_webvitals_enabled: false
    # Api Key, only applies to Grafana Javascript Agent provider
    api_key: testApiKey
```
