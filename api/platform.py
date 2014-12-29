__author__ = 'pgladkov'

from api.validation import validate_json
import unittest


class JsonRpcPlatform(unittest.TestCase):

    def assertJsonStructure(self, method, structure=None):

        assert getattr(method, 'structure', None) or structure, \
            'Specify "structure" property in %s ' % method.__class__ + \
            'or pass "structure" param into assertStructure'
        errors = validate_json(
            structure or method.structure,
            method.result,
            cls=method.validation_class if hasattr(method, 'validation_class') else None
        )
        if errors:
            raise self.failureException(errors)