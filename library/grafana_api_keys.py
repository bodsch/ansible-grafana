#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) 2022, Bodo Schulz <bodo@boone-schulz.de>

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule

import urllib3
import json
import requests


class GrafanaAPI(object):
    """
    """

    def __init__(self, module):
        """
          Initialize all needed Variables
        """
        self.module = module

        self.state = module.params.get("state")
        self.grafana_url = module.params.get("grafana_url")
        self.grafana_admin = module.params.get("grafana_admin")
        self.grafana_api_keys = module.params.get("api_keys")

        self.grafana_admin_user = self.grafana_admin.get("username", None)
        self.grafana_admin_pass = self.grafana_admin.get("password", None)

        self._grafana_cli = module.get_bin_path("grafana-cli", True)

    def run(self):
        """
          runner
        """
        result = dict(
            rc=0,
            failed=False,
            changed=False,
            msg="Grafana API ..."
        )

        if self.state == "list":
            r = self.list_api_keys()

            result = dict(
                rc=0,
                failed=False,
                changed=False,
                msg="Existing API Keys",
                api_keys=r
            )
        if self.state == "manage":
            """
            """
            res = {}
            self.module.log(msg=f" all      : {self.grafana_api_keys} / {type(self.grafana_api_keys)}")

            present_keys = [v for v in self.grafana_api_keys if v.get('state', "present") == "present"]
            absent_keys  = [v for v in self.grafana_api_keys if v.get('state', "present") == "absent"]
            disabled_keys = [v for v in self.grafana_api_keys if v.get('state', "present") == "disabled"]

            # self.module.log(msg=f" present  : {present_keys}")
            # self.module.log(msg=f" absent   : {absent_keys}")
            # self.module.log(msg=f" disabled : {disabled_keys}")

            existing_api_keys = self.list_api_keys()
            existing_key_names = [d['name'] for d in existing_api_keys]
            existing_key_names_with_id = {d['name']: d['id'] for d in existing_api_keys}

            # self.module.log(msg=f" - {existing_key_names}")

            for a in absent_keys:
                _name = a.get("name", None)
                if _name in existing_key_names:
                    _id = existing_key_names_with_id.get(_name)

                    error, msg = self.remove_api_key(_id)
                    res[_name] = dict(
                        msg=msg,
                        state=self.state,
                        failed=error,
                        changed=True
                    )
                else:
                    res[_name] = dict(
                        msg=f"api key for {_name} not exists.",
                        state=self.state,
                        failed=False,
                        changed=False
                    )

            for p in present_keys:
                _name = p.get("name", None)

                if _name in existing_key_names:
                    res[_name] = dict(
                        msg=f"api key for {_name} already created.",
                        state=self.state,
                        failed=False,
                        changed=False
                    )
                else:
                    error, msg = self.create_api_key(p)
                    res[_name] = dict(
                        result=msg,
                        state=self.state,
                        failed=error
                    )

            self.module.log(msg=f" = {res}")

            changed = (len({k: v for k, v in res.items() if v.get('changed')}) > 0)
            failed = (len({k: v for k, v in res.items() if v.get('failed')}) > 0)

            self.module.log(msg=f" changed:  {changed}")
            self.module.log(msg=f" failed :  {failed}")

            result = dict(
                failed=failed,
                changed=changed,
                result=res
            )

        return result

    def list_api_keys(self):
        """
            http://127.0.0.1:3000/api/auth/keys
        """

        status_code, text = self.__call_url()

        if status_code == 200:
            return text
        else:
            return None

        pass

    def create_api_key(self, data):
        """
        """
        self.module.log(msg=f"create_api_key(self, {data})")

        api_name = data.get("name", None)
        api_role = data.get("role", "Viewer")
        api_expiration = data.get("expiration", None)

        if not api_name:
            msg = "missing api name"
            return True, msg

        if api_role not in ["Viewer", "Editor", "Admin"]:
            msg = f"wrong API role '{api_role}'. Can be one of the following values: Viewer, Editor or Admin."
            return True, msg

        payload = dict(
            name=api_name,
            role=api_role
        )

        if api_expiration:
            payload.update({"secondsToLive": api_expiration})

        self.module.log(msg=f" - payload {payload}")

        status_code, text = self.__call_url(method="POST", data=payload)

        if status_code == 200:
            return False, text
        else:
            return True, text

        pass

    def remove_api_key(self, id):
        """
        """
        self.module.log(msg=f"remove_api_key(self, {id})")

        status_code, text = self.__call_url(method="DELETE", key_id=id)

        if status_code == 200:
            return False, text
        else:
            return True, text

    def __call_url(self, method='GET', data=None, key_id=None):
        """
        """
        self.module.log(msg=f"__call_url(self, {method}, {data}, {key_id})")

        response = None

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        # self.module.log(msg="------------------------------------------------------------------")
        # self.module.log(msg=f" method : {method}")
        # self.module.log(msg=f" data   : {data}")
        # self.module.log(msg=f" headers: {headers}")

        try:
            authentication = (self.grafana_admin_user, self.grafana_admin_pass)
            if method == 'POST':
                response = requests.post(
                    f"{self.grafana_url}/api/auth/keys",
                    data=json.dumps(data),
                    headers=headers,
                    auth=authentication
                )
            elif method == "GET":
                response = requests.get(
                    f"{self.grafana_url}/api/auth/keys",
                    headers=headers,
                    auth=authentication
                )
            elif method == "DELETE":
                if key_id:
                    response = requests.delete(
                        f"{self.grafana_url}/api/auth/keys/{key_id}",
                        headers=headers,
                        auth=authentication
                    )

            else:
                self.module.log(msg="unsupported")
                pass

            # response.raise_for_status()

            # self.module.log(msg=f" text    : {response.text} / {type(response.text)}")
            # self.module.log(msg=f" json    : {response.json()} / {type(response.json())}")
            # self.module.log(msg=f" headers : {response.headers}")
            # self.module.log(msg=f" code    : {response.status_code}")
            # self.module.log(msg="------------------------------------------------------------------")

            return response.status_code, response.json()

        except requests.exceptions.HTTPError as e:
            self.module.log(msg=f"ERROR   : {e}")

            status_code = e.response.status_code
            status_message = e.response.json()
            # self.module.log(msg=f" status_message : {status_message} / {type(status_message)}")
            # self.module.log(msg=f" status_message : {e.response.json()}")

            if status_message.get("message") == "Not found":
                status_message = f"API id {key_id} not found."

            return status_code, status_message

        except Exception as e:
            self.module.log(msg=f"ERROR   : {e}")
            # self.module.log(msg=f" text    : {response.text} / {type(response.text)}")
            # self.module.log(msg=f" json    : {response.json()} / {type(response.json())}")
            # self.module.log(msg=f" headers : {response.headers}")
            # self.module.log(msg=f" code    : {response.status_code}")
            # self.module.log(msg="------------------------------------------------------------------")

            return response.status_code, response.json()

        # ===========================================
# Module execution.
#


def main():
    """
    """
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(
                default="list",
                choices=["list", "manage"]
            ),
            grafana_url=dict(
                required=False,
                type="str",
                default="http://127.0.0.1:3000"
            ),
            grafana_admin=dict(
                required=True,
                type="dict"
            ),
            api_keys=dict(
                required=False,
                type="list"
            ),
        ),
        supports_check_mode=False,
    )

    o = GrafanaAPI(module)
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
