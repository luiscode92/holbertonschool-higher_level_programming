#!/usr/bin/python3
"""
save  json file module
"""


def save_to_json_file(my_obj, filename):
    """writing and object to a text using json rep"""
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
