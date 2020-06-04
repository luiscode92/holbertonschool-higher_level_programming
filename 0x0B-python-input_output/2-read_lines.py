#!/usr/bin/python3
"""
red line module
"""


def read_lines(filename="", nb_lines=0):
    """read n lines of a text file"""
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
            return
        count = 0
        for line in f:
            if count < nb_lines:
                print(line, end='')
            count += 1
