# `grafana_config_plugin`

> Not implemented yet.
> Needs support!

```yaml
grafana_config_plugin:
  #################################### Grafana Image Renderer Plugin ##########################
  grafana-image-renderer:
    # Instruct headless browser instance to use a default timezone when not provided by Grafana, e.g. when rendering panel image of alert.
    # See ICU<E2><80><99>s metaZones.txt (https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt) for a list of supported
    # timezone IDs. Fallbacks to TZ environment variable if not set.
    rendering_timezone: ""

    # Instruct headless browser instance to use a default language when not provided by Grafana, e.g. when rendering panel image of alert.
    # Please refer to the HTTP header Accept-Language to understand how to format this value, e.g. 'fr-CH, frq=0.9, enq=0.8, deq=0.7, *q=0.5'.
    rendering_language: ""

    # Instruct headless browser instance to use a default device scale factor when not provided by Grafana, e.g. when rendering panel image of alert.
    # Default is 1. Using a higher value will produce more detailed images (higher DPI), but will require more disk space to store an image.
    rendering_viewport_device_scale_factor: ""

    # Instruct headless browser instance whether to ignore HTTPS errors during navigation. Per default HTTPS errors are not ignored. Due to
    # the security risk it's not recommended to ignore HTTPS errors.
    rendering_ignore_https_errors: ""

    # Instruct headless browser instance whether to capture and log verbose information when rendering an image. Default is false and will
    # only capture and log error messages. When enabled, debug messages are captured and logged as well.
    # For the verbose information to be included in the Grafana server log you have to adjust the rendering log level to debug, configure
    # [log].filter: "" rendering:debug.
    rendering_verbose_logging: ""

    # Instruct headless browser instance whether to output its debug and error messages into running process of remote rendering service.
    # Default is false. This can be useful to enable (true) when troubleshooting.
    rendering_dumpio: ""

    # Additional arguments to pass to the headless browser instance. Default is --no-sandbox. The list of Chromium flags can be found
    # here (https://peter.sh/experiments/chromium-command-line-switches/). Multiple arguments is separated with comma-character.
    rendering_args: ""

    # You can configure the plugin to use a different browser binary instead of the pre-packaged version of Chromium.
    # Please note that this is not recommended, since you may encounter problems if the installed version of Chrome/Chromium is not
    # compatible with the plugin.
    rendering_chrome_bin: ""

    # Instruct how headless browser instances are created. Default is 'default' and will create a new browser instance on each request.
    # Mode 'clustered' will make sure that only a maximum of browsers/incognito pages can execute concurrently.
    # Mode 'reusable' will have one browser instance and will create a new incognito page on each request.
    rendering_mode: ""

    # When rendering_mode: "" clustered, you can instruct how many browsers or incognito pages can execute concurrently. Default is 'browser'
    # and will cluster using browser instances.
    # Mode 'context' will cluster using incognito pages.
    rendering_clustering_mode: ""
    # When rendering_mode: "" clustered, you can define the maximum number of browser instances/incognito pages that can execute concurrently. Default is '5'.
    rendering_clustering_max_concurrency: ""
    # When rendering_mode: "" clustered, you can specify the duration a rendering request can take before it will time out. Default is `30` seconds.
    rendering_clustering_timeout: ""

    # Limit the maximum viewport width, height and device scale factor that can be requested.
    rendering_viewport_max_width: ""
    rendering_viewport_max_height: ""
    rendering_viewport_max_device_scale_factor: ""

    # Change the listening host and port of the gRPC server. Default host is 127.0.0.1 and default port is 0 and will automatically assign
    # a port not in use.
    grpc_host: ""
    grpc_port: ""
```
