#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) 2022, Bodo Schulz <bodo@boone-schulz.de>

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule

from requests.exceptions import ConnectionError
import json
import requests


"""
grafana_organisations:
  molecule: {}
  "Master Inc.": {}
"""


class GrafanaOrganisation(object):
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
        self.organisation = module.params.get("organisation")

        self.grafana_admin_user = self.grafana_admin.get("username", None)
        self.grafana_admin_pass = self.grafana_admin.get("password", None)

    def run(self):
        """
          runner
        """
        result = dict(
            rc=0,
            failed=False,
            changed=False,
            msg="Grafana organisation  ..."
        )

        error, existing_organisation = self.get_organisation(self.organisation)

        if error:
            return dict(
                failed=True,
                changed=False,
                result=existing_organisation
            )

        if self.state == "absent":
            """
            """

            pass

        if self.state == "present":
            """
            """

            pass


        return result

    def get_organisation(self, name):
        """
            https://grafana.com/docs/grafana/latest/developers/http_api/org/#get-organization-by-name
            http://127.0.0.1:3000/api/orgs/name/$NAME
        """
        error = True
        output = None

        status_code, output = self.__call_url(org_name=name)

        if status_code == 200:
            error = False

        self.module.log(msg=f" - error   {error}")
        self.module.log(msg=f" - output  {output}")

        return error, output

    def create_organisation(self, data):
        """
            https://grafana.com/docs/grafana/latest/developers/http_api/org/#create-organization
        """
        self.module.log(msg=f"create_organisation(self, {data})")

        pass

    def remove_organisation(self, id):
        """
            https://grafana.com/docs/grafana/latest/developers/http_api/org/#delete-organization
        """

        pass

    def __call_url(self, method='GET', data=None, org_name=None):
        """
        """
        self.module.log(msg=f"__call_url(self, {method}, {data}, {org_name})")

        response = None

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            authentication = (self.grafana_admin_user, self.grafana_admin_pass)
            if method == 'POST':
                response = requests.post(
                    f"{self.grafana_url}/api/orgs",
                    data=json.dumps(data),
                    headers=headers,
                    auth=authentication
                )
            elif method == "GET":
                response = requests.get(
                    f"{self.grafana_url}/api/orgs/{org_name}",
                    headers=headers,
                    auth=authentication
                )
            elif method == "DELETE":
                if key_id:
                    response = requests.delete(
                        f"{self.grafana_url}/api/orgs/{org_name}",
                        headers=headers,
                        auth=authentication
                    )

            else:
                self.module.log(msg="unsupported")
                pass

            response.raise_for_status()

            return response.status_code, response.json()

        except requests.exceptions.HTTPError as e:
            self.module.log(msg=f"ERROR   : {e}")

            status_code = e.response.status_code
            status_message = e.response.json()

            if status_message.get("message") == "Not found":
                status_message = f"API id {key_id} not found."

            return status_code, status_message

        except ConnectionError as e:
            error_text = f"{type(e).__name__} {(str(e) if len(e.args) == 0 else str(e.args[0]))}"
            self.module.log(msg=f"ERROR   : {error_text}")

            return 500, error_text

        except Exception as e:
            self.module.log(msg=f"ERROR   : {e}")

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
                choices=["list", "present", "absent"],
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
            organisation=dict(
                required=True,
                type="dict"
            ),
        ),
        supports_check_mode=False,
    )

    o = GrafanaOrganisation(module)
    result = o.run()

    module.log(msg=f"= result: {result}")

    module.exit_json(**result)


# import module snippets
if __name__ == '__main__':
    main()
