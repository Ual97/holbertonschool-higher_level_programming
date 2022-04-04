#!/usr/bin/python3
"""
Module 2-is_same_class

a function that returns True if object is an instance
of the specified class
"""


def is_same_class(obj, a_class):
    """
    returns True or False, given by the object
    """
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
