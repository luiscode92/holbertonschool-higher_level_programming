#!/usr/bin/python3
"""
This module provides a simple Square class with initialize size.
"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """return area of a square"""
        return self.__size**2

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)    
