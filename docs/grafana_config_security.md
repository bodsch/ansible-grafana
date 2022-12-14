# `grafana_config_security`

> Not implemented yet.
> Needs support!

```yaml
grafana_config_security:
  # disable creation of admin user on first start of grafana
  disable_initial_admin_creation: false
  # default admin user, created on startup
  admin_user: admin
  # default admin password, can be changed before first start of grafana,  or in profile settings
  admin_password: admin
  # used for signing
  secret_key: SW2YcwTIb9zpOOhoPsMm
  # current key provider used for envelope encryption, default to static value specified by secret_key
  encryption_provider: secretKey.v1
  # list of configured key providers, space separated (Enterprise only): e.g., awskms.v1 azurekv.v1
  available_encryption_providers: ""
  # disable gravatar profile images
  disable_gravatar: false
  # data source proxy whitelist (ip_or_domain:port separated by spaces)
  data_source_proxy_whitelist: ""
  # disable protection against brute force login attempts
  disable_brute_force_login_protection: false
  # set to true if you host Grafana behind HTTPS. default is false.
  cookie_secure: false
  # set cookie SameSite attribute. defaults to `lax`. can be set to "lax", "strict", "none" and "disabled"
  cookie_samesite: lax
  # set to true if you want to allow browsers to render Grafana in a <frame>, <iframe>, <embed> or <object>. default is false.
  allow_embedding: false
  # Set to true if you want to enable http strict transport security (HSTS) response header.
  # HSTS tells browsers that the site should only be accessed using HTTPS.
  strict_transport_security: false
  # Sets how long a browser should cache HSTS. Only applied if strict_transport_security is enabled.
  strict_transport_security_max_age_seconds: 86400
  # Set to true if to enable HSTS preloading option. Only applied if strict_transport_security is enabled.
  strict_transport_security_preload: false
  # Set to true if to enable the HSTS includeSubDomains option. Only applied if strict_transport_security is enabled.
  strict_transport_security_subdomains: false
  # Set to true to enable the X-Content-Type-Options response header.
  # The X-Content-Type-Options response HTTP header is a marker used by the server to indicate that the MIME types advertised
  # in the Content-Type headers should not be changed and be followed.
  x_content_type_options: true
  # Set to true to enable the X-XSS-Protection header, which tells browsers to stop pages from loading
  # when they detect reflected cross-site scripting (XSS) attacks.
  x_xss_protection: true
  # Enable adding the Content-Security-Policy header to your requests.
  # CSP allows to control resources the user agent is allowed to load and helps prevent XSS attacks.
  content_security_policy: false
  # Set Content Security Policy template used when adding the Content-Security-Policy header to your requests.
  # $NONCE in the template includes a random nonce.
  # $ROOT_PATH is server.root_url without the protocol.
  content_security_policy_template:
    script-src:
      - self
      - unsafe-eval
      - unsafe-inline
      - strict-dynamic
      - "$NONCE"
    object-src:
      - none
    font-src:
      - self
    style-src:
      - self
      - unsafe-inline
      - "blob:"
    img-src:
      - "*"
      - "data:"
    base-uri:
      - self
    connect-src:
      - self
      - grafana.com
      - ws://$ROOT_PATH
      - wss://$ROOT_PATH
    manifest-src:
      - self
    media-src:
      - none
    form-action:
      - self

  # Controls if old angular plugins are supported or not. This will be disabled by default in future release
  angular_support_enabled: true
  # List of additional allowed URLs to pass by the CSRF check, separated by spaces. Suggested when authentication comes from an IdP.
  csrf_trusted_origins: example.com
  # List of allowed headers to be set by the user, separated by spaces. Suggested to use for if authentication lives behind reverse proxies.
  csrf_additional_headers: ""

  encryption:
    # Defines the time-to-live (TTL) for decrypted data encryption keys stored in memory (cache).
    # Please note that small values may cause performance issues due to a high frequency decryption operations.
    data_keys_cache_ttl: 15m

    # Defines the frequency of data encryption keys cache cleanup interval.
    # On every interval, decrypted data encryption keys that reached the TTL are removed from the cache.
    data_keys_cache_cleanup_interval: 1m
```
