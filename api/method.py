__author__ = 'pgladkov'

import requests
from json import dumps, loads
import urllib


class JsonRpcMethod(object):

    SUPPORTED_VERSIONS = {'1.0', '1.1', '2.0'}
    VERSION = '2.0'
    HTTP_METHOD = 'POST'
    id = None
    method = None
    params = None
    result = None
    error = None

    structure = {}
    get_params = None

    _response = None

    def __init__(self, test_case):
        """
        :type test_case: Config
        :return:
        """
        self._http_method = self.HTTP_METHOD.lower()
        self.test_case = test_case
        self.url = test_case.url
        self.result = None

    def get_body(self, params):
        self.params = params
        body = {
            'method': self.method,
            'id': self.id,
            'params': params or [],
        }
        if self.VERSION == '2.0':
            body['jsonrpc'] = self.VERSION
        elif self.VERSION == '1.1':
            body['version'] = self.VERSION
        return dumps(body)

    def get_url(self):
        url = self.url + '?'
        return ''.join([url, urllib.urlencode(self.get_params)])

    def call(self, params=None):
        body = dumps(loads(
            self.get_body(params)
        ), indent=4)
        self._response = getattr(requests, self._http_method)(
            self.get_url(), data=body,
            headers={'content-type': 'application/json'},
            verify=False
        )
        self.parse_response()

    def parse_response(self):

        try:
            json = self._response.json()
        except ValueError as e:
            raise Exception(
                u'Incorrect JSON response with status code: %s [%s: %s] \n%s'
                % (
                    self._response.status_code,
                    e.__class__.__name__,
                    e.message,
                    self._response.content
                )
            )
        if 'error' not in json and 'result' not in json:
            raise AssertionError(
                'Incorrect JSON-RPC response: at least one of "error" and "result" fields must be in the response'
            )
        self.result = json.get('result')
        self.error = json.get('error')