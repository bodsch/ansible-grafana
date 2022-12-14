# `grafana_config_dataproxy`

```yaml
grafana_config_dataproxy:
  enabled: false
  # This enables data proxy logging, default is false
  logging: false
  # How long the data proxy waits to read the headers of the response before timing out, default is 30 seconds.
  # This setting also applies to core backend HTTP data sources where query requests use an HTTP client with timeout set.
  timeout: 30
  # How long the data proxy waits to establish a TCP connection before timing out, default is 10 seconds.
  dialTimeout: 10
  # How many seconds the data proxy waits before sending a keepalive probe request.
  keep_alive_seconds: 30
  # How many seconds the data proxy waits for a successful TLS Handshake before timing out.
  tls_handshake_timeout_seconds: 10
  # How many seconds the data proxy will wait for a server's first response headers after
  # fully writing the request headers if the request has an "Expect: 100-continue"
  # header. A value of 0 will result in the body being sent immediately, without
  # waiting for the server to approve.
  expect_continue_timeout_seconds: 1
  # Optionally limits the total number of connections per host, including connections in the dialing,
  # active, and idle states. On limit violation, dials will block.
  # A value of zero (0) means no limit.
  max_conns_per_host: 0
  # The maximum number of idle connections that Grafana will keep alive.
  max_idle_connections: 100
  # How many seconds the data proxy keeps an idle connection open before timing out.
  idle_conn_timeout_seconds: 90
  # If enabled and user is not anonymous, data proxy will add X-Grafana-User header with username into the request, default is false.
  send_user_header: false
  # Limit the amount of bytes that will be read/accepted from responses of outgoing HTTP requests.
  response_limit: 0
  # Limits the number of rows that Grafana will process from SQL data sources.
  row_limit: 1000000
```
