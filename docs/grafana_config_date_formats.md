# `grafana_config_date_formats`

```yaml
grafana_config_date_formats:
  enabled: true
  # For information on what formatting patterns that are supported https://momentjs.com/docs/#/displaying/
  # Default system date format used in time range picker and other places where full time is displayed
  full_date: YYYY-MM-DD HH:mm:ss
  # Used by graph and other places where we only show small intervals
  interval_second: HH:mm:ss
  interval_minute: HH:mm
  interval_hour: MM/DD HH:mm
  interval_day: MM/DD
  interval_month: YYYY-MM
  interval_year: YYYY
  # Experimental feature
  use_browser_locale: false
  # Default timezone for user preferences.
  # Options are 'browser' for the browser local timezone or a timezone name from IANA Time Zone database, e.g. 'UTC' or 'Europe/Amsterdam' etc.
  default_timezone: browser
```
