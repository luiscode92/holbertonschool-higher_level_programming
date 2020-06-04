#!/usr/bin/python3
"""
Read file module
"""


def read_file(filename=""):
    """Print content of text file"""
    with open(filename, 'r') as f:
        print(f.read(), end='')