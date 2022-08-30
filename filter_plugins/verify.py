# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
      ansible filter
    """

    def filters(self):
        return {
            'compare_list': self.compare_list,
            'validate_attachment_hash': self.validate_attachment_hash,
            'validate_datasource_type': self.validate_datasource_type,
            'absent_datasources': self.absent_datasources,
            'non_existing_api': self.non_existing_api,
        }

    def compare_list(self, data_list, compare_to_list):
        """
        """
        display.v(f"compare_list({data_list}, {compare_to_list})")

        result = []

        for i in data_list:
            if i in compare_to_list:
                result.append(i)

        display.v(f"return : {result}")
        return result

    def validate_attachment_hash(self, data, compare_to_list):
        """

        """
        display.v(f"validate_attachment_hash({data}, {compare_to_list})")

        if ':' in data:
            for i in compare_to_list:
                if i[:-1] in data:
                    return True
        else:
            if data in compare_to_list:
                return True

        return False

    def validate_datasource_type(self, data):
        """
        """
        result = True

        return result

    def absent_datasources(self, data):
        """
        """
        result = []

        _data = data.copy()

        for datasource, values in _data.items():
            res = {}
            if values.get("state") == "absent":
                res = dict(
                    name = datasource,
                    orgId = values.get("orgId", 1)
                )
                result.append(res)

                _ = data.pop(datasource)

        return data, result

    def non_existing_api(self, data, existing_api_keys):
        """
        """
        display.v(f"non_existing_api({data}, {existing_api_keys})")
        result = []

        names = []

        for d in existing_api_keys:
            names.append(d.get("name"))

        display.v(f"names {names}")

        #names = {k: v for k, v in data.items() if v.get('name')}

        for e in data:
            _name = e.get("name")
            display.v(f"- name {_name}")

            if _name in names or _name == "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER":
                continue
            else:
                result.append(e)

        display.v(f" = result {result}")

        return result
