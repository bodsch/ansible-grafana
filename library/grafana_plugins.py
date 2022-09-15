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
            msg="Grafana Plugins ..."
        )

    def _list(self):
      """
        # grafana-cli plugins ls --help
        NAME:
           Grafana CLI plugins ls - list all installed plugins

        USAGE:
           Grafana CLI plugins ls [command options] [arguments...]
      """
      pass

    def _list_remote(self):
      """
        # grafana-cli plugins list-remote --help
        NAME:
           Grafana CLI plugins list-remote - list remote available plugins

        USAGE:
           Grafana CLI plugins list-remote [command options] [arguments...]
      """
      pass

    def _list_versions(self):
      """
        # grafana-cli plugins list-versions --help
        NAME:
           Grafana CLI plugins list-versions - list-versions <plugin id>

        USAGE:
           Grafana CLI plugins list-versions [command options] [arguments...]
      """
      pass

    def _update(self):
      """
        # grafana-cli plugins update --help
        NAME:
           Grafana CLI plugins update - update <plugin id>

        USAGE:
           Grafana CLI plugins update [command options] [arguments...]
      """
      pass

    def _update_all(self):
      """
        # grafana-cli plugins update-all --help
        NAME:
           Grafana CLI plugins update-all - update all your installed plugins

        USAGE:
           Grafana CLI plugins update-all [command options] [arguments...]
      """
      pass

    def _install(self):
      """
        # grafana-cli plugins install --help
        NAME:
           Grafana CLI plugins install - install <plugin id> <plugin version (optional)>

        USAGE:
           Grafana CLI plugins install [command options] [arguments...]
      """
      pass

    def _uninstall(self):
      """
        # grafana-cli plugins uninstall --help
        NAME:
           Grafana CLI plugins uninstall - uninstall <plugin id>

        USAGE:
           Grafana CLI plugins uninstall [command options] [arguments...]
      """
      pass



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

    o = GrafanaCLI(module)
    result = o.run()

    module.log(msg=f"= result: {result}")

    module.exit_json(**result)


# import module snippets
if __name__ == '__main__':
    main()


"""
# grafana-cli plugins --help
NAME:
   Grafana CLI plugins - Manage plugins for grafana

USAGE:
   Grafana CLI plugins command [command options] [arguments...]

COMMANDS:
   install                  install <plugin id> <plugin version (optional)>
   list-remote              list remote available plugins
   list-versions            list-versions <plugin id>
   update, upgrade          update <plugin id>
   update-all, upgrade-all  update all your installed plugins
   ls                       list all installed plugins
   uninstall, remove        uninstall <plugin id>
   help, h                  Shows a list of commands or help for one command

OPTIONS:
   --help, -h  show help (default: false)
"""
