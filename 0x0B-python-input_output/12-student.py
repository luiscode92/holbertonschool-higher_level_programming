#!/usr/bin/python3
"""
students module
"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict representation of a student"""
        if attrs is None:
            return self.__dict__
        my_attrs = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                my_attrs[key] = value
        return my_attrs
