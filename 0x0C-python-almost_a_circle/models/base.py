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
        
