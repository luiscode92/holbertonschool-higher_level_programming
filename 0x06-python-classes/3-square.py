#!/usr/bin/python3
"""
This module provides a simple Square class with initialize size.
"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size**2
