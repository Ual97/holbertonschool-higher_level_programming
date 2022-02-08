#!/usr/bin/python3
"""
Base class, with private class attribute __nb_objects = 0
and class constructor __init__
"""

import json
import csv


class Base():
    """Class base:
    attributes:
        __nb_objects
    methods:
        __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation of a string"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON representation of list_objs to a file"""
        obj = []
        if list_objs is not None:
            for o in list_objs:
                obj.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(obj))
