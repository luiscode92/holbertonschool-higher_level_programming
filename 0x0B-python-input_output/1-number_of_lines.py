#!/usr/bin/python3
"""
number of lines module
"""


def number_of_lines(filename=""):
    """count the number of lines ins a text file"""
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += 1
    return count
