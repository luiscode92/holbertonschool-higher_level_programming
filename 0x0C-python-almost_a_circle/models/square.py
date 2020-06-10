#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represent a rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print square sttr"""
        return ('[Square] (' +
                str(self.id) +
                ') ' +
                str(self._Rectangle__x) +
                '/' +
                str(self._Rectangle__y) +
                ' - ' +
                str(self._Rectangle__width))

    @property
    def size(self):
        """get the size"""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """set the size"""
        self.integer_validator('width', value)
        self.integer_validator('height', value)
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """ update the square"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self._Rectangle__x = args[2]
            if len(args) >= 4:
                self._Rectangle__y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary rep of rectangle"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self._Rectangle__x,
            'y': self._Rectangle__y}
