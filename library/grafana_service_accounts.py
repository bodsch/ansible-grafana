#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) 2022, Bodo Schulz <bodo@boone-schulz.de>

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.bodsch.core.plugins.module_utils.directory import create_directory

import os
import json
import requests
from requests.exceptions import ConnectionError
from pathlib import Path


class GrafanaServiceAccount(object):
    """
    """
    def __init__(self, module):
        """
        """
        self.module = module

        self.state = module.params.get("state")
        self.grafana_url = module.params.get("grafana_url")
        self.grafana_admin = module.params.get("grafana_admin")
        self.grafana_api_token = module.params.get("api_token")
        self.grafana_org_id = module.params.get("org_id")
        self.grafana_service_accounts = module.params.get("service_accounts")

        self.grafana_admin_user = self.grafana_admin.get("username", None)
        self.grafana_admin_pass = self.grafana_admin.get("password", None)

        self.apikey_directory = f"{Path.home()}/.ansible/cache/grafana"

    def run(self):
        """
        """
        result = dict(
            rc=0,
            failed=False,
            changed=False,
            msg="Grafana service accounts  ..."
        )

        create_directory(directory=self.apikey_directory, mode="0750")

        if self.state == "list":
            error, msg = self.list_service_accounts()

            if error:
                result = dict(
                    failed=True,
                    changed=False,
                    msg=msg
                )
            else:
                result = dict(
                    rc=0,
                    failed=False,
                    changed=False,
                    msg="Existing Service Accounts",
                    service_accounts=msg
                )

        if self.state == "manage":
            """
            """
            res = {}
            self.module.log(msg=f" account       : {self.grafana_service_accounts}")

            present_keys = [v for v in self.grafana_service_accounts if v.get('state', "present") == "present"]
            absent_keys  = [v for v in self.grafana_service_accounts if v.get('state', "present") == "absent"]
            # disabled_keys = [v for v in self.grafana_service_accounts if v.get('state', "present") == "disabled"]

            self.module.log(msg=f" must present  : {present_keys}")
            self.module.log(msg=f" must absent   : {absent_keys}")
            # self.module.log(msg=f" disabled : {disabled_keys}")

            error, existing_service_accounts = self.list_service_accounts()

            if error:
                return dict(
                    failed=True,
                    changed=False,
                    result=existing_service_accounts
                )

            """
                {
                    'count': 2,
                    'service_account': [
                        {'id': 2, 'name': 'backup-service-account', 'login': 'sa-backup-service-account', 'orgId': 1, 'isDisabled': False, 'role': 'Admin', 'tokens': 0, 'avatarUrl': '/public/img/user_profile.png'},
                        {'id': 3, 'name': 'sa-importer', 'login': 'sa-sa-importer', 'orgId': 1, 'isDisabled': False, 'role': 'Viewer', 'tokens': 0, 'avatarUrl': '/public/img/user_profile.png'}
                    ]
                }
            """

            existing_service_accounts = existing_service_accounts.get("service_accounts", [])

            existing_key_names = [d['name'] for d in existing_service_accounts]
            existing_key_names_with_id = {d['name']: d['id'] for d in existing_service_accounts}

            self.module.log(msg=f" -  existing #2 {existing_key_names}")
            self.module.log(msg=f" -  existing #2 {existing_key_names_with_id}")

            existing_service_tokens = self.service_tokens(existing_key_names_with_id)

            # self.module.log(msg=f" - {existing_key_names}")

            for a in absent_keys:
                _name = a.get("name", None)
                if _name in existing_key_names:
                    _id = existing_key_names_with_id.get(_name)

                    error, msg = self.remove_api_key(_id)
                    res[_name] = dict(
                        msg=msg,
                        state="absent",
                        failed=error,
                        changed=True
                    )
                else:
                    res[_name] = dict(
                        msg=f"api key for {_name} not exists.",
                        state="absent",
                        failed=False,
                        changed=False
                    )

            for p in present_keys:
                _name = p.get("name", None)
                if _name in existing_key_names:
                    res[_name] = dict(
                        msg=f"api key for {_name} already created.",
                        state="present",
                        failed=False,
                        changed=False
                    )
                else:
                    error, msg = self.create_api_key(p)
                    res[_name] = dict(
                        result=msg,
                        state="present",
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

    def list_service_accounts(self):
        """
            http://127.0.0.1:3000/api/serviceaccounts
        """
        error = True
        output = None
        total_count = 0
        service_accounts = []

        status_code, output = self.__call_url(path="search")

        if status_code == 200:
            error = False
            total_count = output.get("totalCount", 0)
            service_accounts = output.get("serviceAccounts", [])

        output = dict(
            count=total_count,
            service_accounts=service_accounts
        )

        self.module.log(msg=f" - error   {error}")
        self.module.log(msg=f" - output  {output}")

        return error, output

    def service_tokens(self, present_keys=[]):
        """
        """
        error = True
        output = None

        for key in present_keys:
            account_id = key.get("id", None)

            if account_id:
                status_code, output = self.__call_url(key_id=account_id)

        return error, output

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
            self.module.log(msg=f" = {text} / {type(text)}")

            key_file = self.save_keyfile(text)

            text.update({"key_file": key_file})
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

    def __call_url(self, method='GET', data=None, path=None, key_id=None):
        """
        """
        self.module.log(msg=f"__call_url(self, {method}, {data}, {path}, {key_id})")

        response = None

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        basic_authentication = None
        if self.grafana_api_token:
            headers["Authorization"] = f"Bearer {self.grafana_api_token}"
        elif self.grafana_admin_user and self.grafana_admin_pass:
            basic_authentication = (self.grafana_admin_user, self.grafana_admin_pass)

        self.module.log(msg="------------------------------------------------------------------")
        self.module.log(msg=f" method : {method}")
        self.module.log(msg=f" data   : {data}")
        self.module.log(msg=f" headers: {headers}")
        self.module.log(msg="------------------------------------------------------------------")

        try:

            if method == 'POST':
                response = requests.post(
                    f"{self.grafana_url}/api/serviceaccounts/{path}",
                    data=json.dumps(data),
                    headers=headers,
                    auth=basic_authentication
                )
            elif method == "GET":
                response = requests.get(
                    f"{self.grafana_url}/api/serviceaccounts/{path}",
                    headers=headers,
                    auth=basic_authentication
                )
            elif method == "DELETE":
                if key_id:
                    response = requests.delete(
                        f"{self.grafana_url}/api/serviceaccounts/{key_id}",
                        headers=headers,
                        auth=basic_authentication
                    )

            else:
                self.module.log(msg="unsupported")
                pass

            response.raise_for_status()

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
                status_message = f"Service Account {key_id} not found."

            return status_code, status_message

        except ConnectionError as e:
            error_text = f"{type(e).__name__} {(str(e) if len(e.args) == 0 else str(e.args[0]))}"
            self.module.log(msg=f"ERROR   : {error_text}")

            self.module.log(msg="------------------------------------------------------------------")
            return 500, error_text

        except Exception as e:
            self.module.log(msg=f"ERROR   : {e}")
            # self.module.log(msg=f" text    : {response.text} / {type(response.text)}")
            # self.module.log(msg=f" json    : {response.json()} / {type(response.json())}")
            # self.module.log(msg=f" headers : {response.headers}")
            # self.module.log(msg=f" code    : {response.status_code}")
            # self.module.log(msg="------------------------------------------------------------------")

            return response.status_code, response.json()

    def save_keyfile(self, data):
        """
            {'id': 1, 'name': 'foo', 'key': 'eyJrIjoiOUtZd29iazRTQ3hsQ0RnbDFSZVpVY2FpZUI4ZEhsZHkiLCJuIjoiZm9vIiwiaWQiOjF9'}
        """
        name = data.get("name", None)
        key = data.get("key", None)

        if name and key:
            file_name = os.path.join(self.apikey_directory, f"{name}.key")

            with open(file_name, "w") as f:
                f.write(key)

            return file_name

        return None


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
            api_token=dict(
                required=False,
                type="str"
            ),
            org_id=dict(
                required=False,
                type="int",
                default=1,
            ),
            service_accounts=dict(
                required=True,
                type="list"
            )
        ),
        supports_check_mode=False,
    )

    o = GrafanaServiceAccount(module)
    result = o.run()

    module.log(msg=f"= result: {result}")

    module.exit_json(**result)


# import module snippets
if __name__ == '__main__':
    main()




"""

SERVICE_ACCOUNT=$(curl \
  --silent \
  --location \
  --request POST \
  --header "Content-Type: application/json" \
  --user "${GRAFANA_ADMIN_USERNAME}:${GRAFANA_ADMIN_PASSWORD}" \
  --data '{"name": "backup-service-account", "role": "Admin"}' \
  http://${GRAFANA_HOST}/api/serviceaccounts)

    SERVICE_ACCOUNT_ID=$(echo "${SERVICE_ACCOUNT}" | jq '.id')

    SERVICE_TOKEN=$(curl --silent --request POST --header "Content-Type: application/json" --data '{"name": "backup-service-account-token"}' \
        http://admin:${GRAFANA_ADMIN_PASSWORD}@${GRAFANA_HOST}/api/serviceaccounts/${SERVICE_ACCOUNT_ID}/tokens)

    TOKEN=$(echo "${SERVICE_TOKEN}" | jq -r '.key')

"""
