#!/usr/bin/python3
"""
Module 3-is_kind_of_class

a function that returns True if object is an instance
of the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    returns True or False, given by the object
    """
    if isinstance(obj, a_class) is True:
        return (True)
    else:
        return (False)
