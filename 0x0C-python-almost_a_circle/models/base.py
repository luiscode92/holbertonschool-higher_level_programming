#!/usr/bin/python3
"""
Base class module
"""
from os import path
import json
import csv


class Base:
    """Represents base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON strin rep of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the json that rep the list_objs to a file."""
        filename = cls.__name__ + '.json'
        dictionary = []
        if list_objs is not None:
            dictionary = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        """retun the list of the json string rep"""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes"""
        if cls.__name__ == 'Rectangle':
            new_base = cls(1, 1)
        else:
            new_base = cls(1)
        cls.update(new_base, **dictionary)
        return new_base

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + '.json'
        if path.isfile(filename):
            with open(filename, 'r') as f:
                my_list = cls.from_json_string(f.read())
            return [cls.create(**obj) for obj in my_list]
        return []