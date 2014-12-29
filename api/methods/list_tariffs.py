__author__ = 'pgladkov'

from api.method import JsonRpcMethod


class ListTariffs(JsonRpcMethod):

    def __init__(self):
        self.method = 'list_tariffs'
        self.get_params = {
            'p': 'nemo.core.user.common',
            'app_name': 'samsung_smarttv_adult'
        }