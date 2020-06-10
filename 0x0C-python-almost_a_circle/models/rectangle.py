#!/usr/bin/python3
"""
Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """print rectangle attributes"""
        return ('[Rectangle] (' + str(self.id) + ') ' + str(self.__x) + '/' + str(self.__y) + ' - ' + str(self.__width) + '/' + str(self.__height))

    def integer_validator(self, attr, value):
        """validate integer"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(attr))
        if value <= 0 and (attr == 'width' or attr == 'height'):
            raise ValueError('{} must be > 0'.format(attr))
        if value < 0 and (attr == 'x' or attr == 'y'):
            raise ValueError('{} must be >=0'.format(attr))

    def area(self):
        """represents the area of a triangle"""
        return self.__width * self.__height

    def display(self):
        """print the rectangle"""
        print('\n' * self.__y + (' ' * self.__x + '#' * self.__width + '\n') * self.__height, end="")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary rep of rectangle"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y}

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set th height"""
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """get the x"""
        return self.__X

    @x.setter
    def x(self, value):
        """set the x"""
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """get the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y"""
        self.integer_validator('y', value)
        self.__y = value  