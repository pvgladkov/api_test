__author__ = 'pgladkov'

import unittest
from api.methods.list_tariffs import ListTariffs
from api.platform import JsonRpcPlatform
from api.config import Config


class TestListTariffs(JsonRpcPlatform):

    def testStructure(self):
        list_tariffs = ListTariffs(Config())
        list_tariffs.call()
        self.assertJsonStructure(list_tariffs)


if __name__ == "__main__":
    unittest.main()