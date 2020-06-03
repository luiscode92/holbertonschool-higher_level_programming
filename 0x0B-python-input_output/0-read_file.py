#!/usr/bin/python3
"""
read file module
"""


def read_file(filename=""):
    """print content of text file"""
    with open(filename, 'r') as f:
        print(f.read(), end='')