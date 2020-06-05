#!/usr/bin/python3
"""
pascal triangle module
"""


def pascal_triangle(n):
    """ return ist that represent pascal's triangle"""
    my_list = []
    if n <= 0:
        return my_list
    for i in range(1, n + 1):
        value = 1
        tmp_list = []
        for j in range(1, i + 1):
            tmp_list.append(str(value))
            value = value * (i - j) // j
        my_list.append(tmp_list)
    return my_list
