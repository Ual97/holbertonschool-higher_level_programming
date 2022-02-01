#!/usr/bin/python3
"""
Module 4-inherits_from
returns True of false given object attributes
"""


def inherits_from(obj, a_class):
    """
   returns true if instance class is object
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))