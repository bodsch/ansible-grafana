#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) 2022, Bodo Schulz <bodo@boone-schulz.de>

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
import json

# since 9.1.x
# replacement for API Keys
# https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/

# look at:
# - https://github.com/m0nhawk/grafana_api/
# - https://github.com/panodata/grafana-client

class GrafanaServiceAccounts(object):
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
            msg="Grafana Plugins ..."
        )




# ===========================================
# Module execution.
#


def main():

    module = AnsibleModule(
        argument_spec=dict(
            command=dict(
                default="ls",
                choices=["install", "list-remote", "list-versions", "update", "upgrade", "update-all", "upgrade-all", "ls", "uninstall", "remove"]
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

    o = GrafanaServiceAccounts(module)
    result = o.run()

    module.log(msg=f"= result: {result}")

    module.exit_json(**result)


# import module snippets
if __name__ == '__main__':
    main()
