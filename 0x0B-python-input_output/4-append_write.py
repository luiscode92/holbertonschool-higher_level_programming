#!/usr/bin/python3
"""
append write file module
"""


def append_write(filename="", text=""):
    """append a string at the end of a text"""
    with open(filename, 'a') as f:
        return f.write(str(text))