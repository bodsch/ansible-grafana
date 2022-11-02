# `grafana_config_server`

```yaml
grafana_config_server:
  # Protocol (http, https, h2, socket)
  protocol: http
  # The ip address to bind to, empty will bind to all interfaces
  http_addr: ""
  # The http port  to use
  http_port: 3000
  # The public facing domain name used to access grafana from a browser
  domain: localhost
  # Redirect to correct domain if host header does not match domain
  # Prevents DNS rebinding attacks
  enforce_domain: false
  # The full public facing url you use in browser, used for redirects and emails
  # If you use reverse proxy and sub path specify full url (with sub path)
  root_url: "%(protocol)s://%(domain)s:%(http_port)s/"
  # Serve Grafana from subpath specified in `root_url` setting. By default it is set to `false` for compatibility reasons.
  serve_from_sub_path: false
  # Log web requests
  router_logging: false
  # the path relative working path
  static_root_path: public
  # enable gzip
  enable_gzip: false
  # https certs & key file
  cert_file: ""
  cert_key: ""
  # Unix socket path
  socket: ""
  # CDN Url
  cdn_url: ""
  # Sets the maximum time using a duration format (5s/5m/5ms) before timing out read of an incoming request and closing idle connections.
  # `0` means there is no timeout for reading the request.
  read_timeout: 0
```
