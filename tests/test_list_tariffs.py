__author__ = 'pgladkov'

import unittest
from api.methods.list_tariffs import ListTariffs
from api.platform import JsonRpcPlatform


class TestListTariffs(JsonRpcPlatform):

    def testStructure(self):
        list_tariffs = ListTariffs()
        list_tariffs.call()

        self.assertJsonStructure(list_tariffs, ListTariffs.structure)


if __name__ == "__main__":
    unittest.main()