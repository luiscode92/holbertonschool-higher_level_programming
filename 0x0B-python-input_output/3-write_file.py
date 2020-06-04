#!/usr/bin/python3
"""
write file module
"""


def write_file(filename="", text=""):
    """write string ina  text."""
    with open(filename, 'w') as f:
        return f.write(str(text))
        