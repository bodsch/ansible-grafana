# `grafana_config_database`

```yaml
grafana_config_database:
  # You can configure the database connection by specifying type, host, name, user and password
  # as separate properties or as on string using the url properties.
  # Either "mysql", "postgres" or "sqlite3", it's your choice
  type: sqlite3
  # For "sqlite3" only, path relative to data_path setting
  path: grafana.db
  # For "sqlite3" only. cache mode setting used for connecting to the database. (private, shared)
  cache_mode: private
  host: 127.0.0.1:3306
  name: grafana
  user: root
  # If the password contains # or ; you have to wrap it with triple quotes. Ex """#password;"""
  password: ""
  # Use either URL or the previous fields to configure the database
  # Example: mysql://user:secret@host:port/database
  url: ""
  # For "postgres" only, either "disable", "require" or "verify-full"
  ssl_mode: disable
  # Database drivers may support different transaction isolation levels.
  # Currently, only "mysql" driver supports isolation levels.
  # If the value is empty - driver's default isolation level is applied.
  # For "mysql" use "READ-UNCOMMITTED", "READ-COMMITTED", "REPEATABLE-READ" or "SERIALIZABLE".
  isolation_level: ""
  ca_cert_path: ""
  client_key_path: ""
  client_cert_path: ""
  server_cert_name: ""
  # Max idle conn setting default is 2
  max_idle_conn: 2
  # Max conn setting default is 0 (mean not set)
  max_open_conn: ""
  # Connection Max Lifetime default is 14400 (means 14400 seconds or 4 hours)
  conn_max_lifetime: 14400
  # Set to true to log the sql calls and execution times.
  log_queries: ""
  # For "mysql" only if migrationLocking feature toggle is set. How many seconds to wait before failing to lock the database for the migrations, default is 0.
  locking_attempt_timeout_sec: 0
```
