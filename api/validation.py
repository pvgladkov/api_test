__author__ = 'pgladkov'


"""
Validator function must returns True (if valid) or False (not valid). Also
validator can raises ValidationError. Convertor function (works on 'type' key)
must returns value or raises ValidationError.
"""
import re
import inspect
from datetime import datetime

from jsonschema import Draft4Validator, Draft3Validator
from jsonschema.exceptions import ValidationError
from json import loads, dumps
import textwrap
import pprint

from jsonschema import _utils

ERROR = 100
WARNING = WARN = 50


def validate_json(schema, instance, cls):
    cls = cls if inspect.isclass(cls) else Draft3Validator
    validator = cls(schema)
    for index, error in enumerate(sorted(validator.iter_errors(instance), key=str)):
        pinstance = pprint.pformat(
            instance[index] if isinstance(instance, list) else instance,
            width=72,
            indent=4,
            depth=3
        )
        path = _utils.format_as_index(error.path)
        schema_path = _utils.format_as_index(list(error.schema_path)[:-1])
        return ('\n' + '='*50 + '\n' + error.message + '\n' + '='*50 + '\n' + textwrap.dedent("""
            Failed validating %r in schema %s:
            On instance with path -> "%s":\n
            %s
            """
        ) % (
            error.validator,
            schema_path,
            path,
            pinstance
        ))