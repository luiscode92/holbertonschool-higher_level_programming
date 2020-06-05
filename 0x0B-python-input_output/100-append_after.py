#!/usr/bin/python3
"""
append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a specific string"""
    with open(filename, 'r') as f:
        text = f.readlines()

    with open(filename, 'w') as f:
        string = ''
        for line in text:
            string += line
            if search_string in line:
                string += new_string
        f.write(string)