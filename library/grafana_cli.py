#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) 2022, Bodo Schulz <bodo@boone-schulz.de>

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
import json


class GrafanaCLI(object):
    """
    """

    def __init__(self, module):
        """
          Initialize all needed Variables
        """
        self.module = module

        self._influx = module.get_bin_path("grafana-cli", True)

    def run(self):
        """
          runner
        """
        result_state = []

        result = dict(
            rc=0,
            failed=False,
            changed=False,
            msg="Influxdb authentications ..."
        )


# ===========================================
# Module execution.
#


def main():

    module = AnsibleModule(
        argument_spec=dict(
            command=dict(
                default="plugins",
                choices=["plugins", "admin"]
            ),
            repo=dict(
                required=False,
                type="str"
            ),
            plugins_dir=dict(
                required=False,
                type="str"
            ),
            plugin_url=dict(
                required=False,
                type="str"
            ),
            insecure=dict(
                required=False,
                type="bool"
            ),
            debug=dict(
                required=False,
                type="bool"
            ),
            homepath=dict(
                required=False,
                type="str"
            ),
            config=dict(
                required=False,
                type="str"
            ),
            config_overrides=dict(
                required=False,
                type="list",
                default=[]
            )
        ),
        supports_check_mode=False,
    )

    o = GrafanaCLI(module)
    result = o.run()

    module.log(msg=f"= result: {result}")

    module.exit_json(**result)


# import module snippets
if __name__ == '__main__':
    main()


"""
# grafana-cli --help
NAME:
   Grafana CLI - A new cli application

USAGE:
   grafana-cli [global options] command [command options] [arguments...]

VERSION:
   9.1.1

AUTHOR:
   Grafana Project <hello@grafana.com>

COMMANDS:
   plugins  Manage plugins for grafana
   admin    Grafana admin commands
   help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --pluginsDir value       Path to the Grafana plugin directory (default: "/var/lib/grafana/plugins") [$GF_PLUGIN_DIR]
   --repo value             URL to the plugin repository (default: "https://grafana.com/api/plugins") [$GF_PLUGIN_REPO]
   --pluginUrl value        Full url to the plugin zip file instead of downloading the plugin from grafana.com/api [$GF_PLUGIN_URL]
   --insecure               Skip TLS verification (insecure) (default: false)
   --debug                  Enable debug logging (default: false)
   --configOverrides value  Configuration options to override defaults as a string. e.g. cfg:default.paths.log=/dev/null
   --homepath value         Path to Grafana install/home path, defaults to working directory
   --config value           Path to config file
   --help, -h               show help (default: false)
   --version, -v            print the version (default: false)
"""
