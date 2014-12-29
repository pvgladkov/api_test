__author__ = 'pgladkov'


class JsonRpcMethod(object):
    SUPPORTED_VERSIONS = {'1.0', '1.1', '2.0'}

    id = None
    method = None
    params = None
    result = None
    error = None

    structure = {}
    get_params = None

    _response = None

    def call(self, params=None):
        pass