#!/usr/bin/python3
"""
json string module
"""


def to_json_string(my_obj):
    """return json representation of an object"""
    import json
    return json.dumps(my_obj)