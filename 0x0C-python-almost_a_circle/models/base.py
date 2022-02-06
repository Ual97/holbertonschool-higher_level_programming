#!/usr/bin/python3
"""
Base class, with private class attribute __nb_objects = 0
and class constructor __init__
"""


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
