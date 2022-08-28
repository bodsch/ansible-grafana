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
        }

    def compare_list(self, data_list, compare_to_list):
        """
        """
        display.v(f"compare_list({data_list}, {compare_to_list})")

        result = []

        for i in data_list:
            if i in compare_to_list:
                result.append(i)

        # randomized result :(
        # result = list(
        #     set(
        #         data_list).intersection(sorted(compare_to_list)
        #     )
        # )

        display.v(f"return : {result}")
        return result

    def validate_attachment_hash(self, data, compare_to_list):
        """

        """
        display.v("validate_attachment_hash({}, {})".format(data, compare_to_list))

        if ':' in data:
            for i in compare_to_list:
                if i[:-1] in data:
                    return True
        else:
            if data in compare_to_list:
                return True

        return False
