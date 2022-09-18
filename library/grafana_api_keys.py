#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) 2022, Bodo Schulz <bodo@boone-schulz.de>

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
import json
from grafana_client import GrafanaApi
from urllib.parse import urlparse

# https://grafana.com/docs/grafana/latest/developers/http_api/auth/#api-keys


class GrafanaAPIKeys(object):
    """
    """

    def __init__(self, module):
        """
          Initialize all needed Variables
        """
        self.module = module

        # self.grafana_server = module.params.get("grafana_server", None)
        # self.grafana_port = module.params.get("grafana_port", None)
        # self.grafana_scheme = module.params.get("grafana_scheme", None)

        self.grafana_url = module.params.get("grafana_url")
        self.grafana_admin = module.params.get("grafana_admin")

        self.grafana_admin_usr = module.params.get("grafana_admin").get("user")
        self.grafana_admin_pass = module.params.get("grafana_admin").get("password")



    def run(self):
        """
          runner
        """
        result_state = []

        result = dict(
            rc=0,
            failed=False,
            changed=False,
            msg="Grafana API Keys ..."
        )

        o = urlparse(self.grafana_url)

        grafana_url = f"{o.scheme}://{self.grafana_admin_usr}:{self.grafana_admin_pass}@{o.hostname}:{o.port}"

        self.module.log(msg=f"  grafana_url      : '{grafana_url}'")

        try:
            grafana = GrafanaApi.from_url(grafana_url)
        except KeyError:
            raise



# ===========================================
# Module execution.
#


def main():

    module = AnsibleModule(
        argument_spec=dict(
            # grafana_server=dict(
            #     required=False,
            #     default="localhost",
            #     type="string"
            # ),
            # grafana_port=dict(
            #     required=False,
            #     default="3000",
            #     type="string"
            # ),
            # grafana_scheme=dict(
            #     required=False,
            #     default="http",
            #     type="string"
            # ),
            grafana_url=dict(
                # required=True,
                default="http://127.0.0.1:3000",
                type="str"
            ),
            grafana_admin=dict(
                required=True,
                type="dict"
            ),
            # plugins_dir=dict(
            #     required=False,
            #     type="str"
            # ),
            # plugin_url=dict(
            #     required=False,
            #     type="str"
            # ),
            # insecure=dict(
            #     required=False,
            #     type="bool"
            # ),
            # debug=dict(
            #     required=False,
            #     type="bool"
            # ),
            # homepath=dict(
            #     required=False,
            #     type="str"
            # ),
            # config=dict(
            #     required=False,
            #     type="str"
            # ),
            # config_overrides=dict(
            #     required=False,
            #     type="list",
            #     default=[]
            # )
        ),
        supports_check_mode=False,
    )

    _adm_user = module.params.get("grafana_admin", {}).get("user")
    _adm_password = module.params.get("grafana_admin", {}).get("password")

    if not _adm_user or not _adm_password:
        module.fail_json(
            msg="Authentication was not specified or was incomplete.",
            rc=1
        )

    o = GrafanaAPIKeys(module)
    result = o.run()

    module.log(msg=f"= result: {result}")

    module.exit_json(**result)


# import module snippets
if __name__ == '__main__':
    main()
