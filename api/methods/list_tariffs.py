__author__ = 'pgladkov'

from api.method import JsonRpcMethod


class ListTariffs(JsonRpcMethod):

    structure = {
        "type": "object",
        "properties": {
            "tarifs": {
                "type": "array"
            }
        }
    }

    method = 'list_tarifs'

    get_params = {
        'p': 'nemo.core.user.common',
        'app_name': 'samsung_smarttv_adult'
    }

    def __init__(self, test_case, params=None):
        super(ListTariffs, self).__init__(test_case)