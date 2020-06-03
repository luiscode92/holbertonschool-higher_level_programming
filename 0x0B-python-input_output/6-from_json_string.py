#!usr/bin/python3
"""
json string module
"""


def from_json_string(my_str):
    """return obj represented by json str"""
    import json
    return json.loads(my_str)