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
            'is_installed': self.is_installed,
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
            if values.get("state", "present") == "absent":
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
        display.v(f"  - {type(data)}")
        display.v(f"  - {type(existing_api_keys)}")

        if len(existing_api_keys) == 0:
            """
              no present API data
            """
            return data

        result = []
        names = []

        for d in existing_api_keys:
            names.append(d.get("name"))

        display.v(f"names {names}")

        for e in data:
            _name = e.get("name")
            display.v(f"- name {_name}")

            if _name in names or _name == "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER":
                continue
            else:
                result.append(e)

        display.v(f" = result {result}")

        return result

    def is_installed(self, data, bin_path):
        """
        """

        # - stat_grafana_path is defined
        # - stat_grafana_path.stat is defined
        # - stat_grafana_path.stat.isdir is defined
        # - not stat_grafana_path.stat.isdir
        # - stat_old_grafana_path is defined
        # - stat_old_grafana_path.stat is defined
        # - stat_old_grafana_path.stat.islnk is defined
        # - not stat_old_grafana_path.stat.islnk

        display.v(f"is_installed({data}, {bin_path})")

        directory = False
        link_to_bin = False

        stat_data = data.get("stat", None)
        stat_bin_path = bin_path.get("stat", None)

        display.v(f"  - {stat_data}")
        display.v(f"  - {stat_bin_path}")

        if stat_data:
            directory = stat_data.get("isdir", False)
            display.v(f"  - {directory}")

        if stat_bin_path:
            link_to_bin = stat_bin_path.get("islnk", False)
            display.v(f"  - {link_to_bin}")

        if directory == False and link_to_bin == False:
            result = True
        else:
            result = False

        display.v(f"return : {result}")
        return result

