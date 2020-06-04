#!/usr/bin/python3
"""
The "read file" module.

Read file module defines one function, read_file().
"""


def read_file(filename=""):
    """Print content of text file"""
    with open(filename, 'r') as f:
        print(f.read(), end='')