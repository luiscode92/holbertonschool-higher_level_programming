#!/usr/bin/python3
"""square coordinaes"""


class Square:
    """square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) != int:
           raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2 or type(value[0]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """return area"""
        return self.__size**2

    def my_print(self):
        """print"""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)    
                