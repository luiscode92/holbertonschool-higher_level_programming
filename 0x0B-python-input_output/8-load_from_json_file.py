#!/usr/bin/python3
"""
load from a json file
"""


def load_from_json_file(filename):
    """create an object from json file"""
    import json
    with open(filename, 'r') as f:
        return json.loads(f.read())