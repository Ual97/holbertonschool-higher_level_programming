#!/usr/bin/python3
"""
Module 0-lookup

contains methos that returns objects attributes and methods
"""


def lookup(obj):
    """
    returns all methods and attributes

    Args:
        obj: instance of class
    Returns:
        List of attributes and methods
    """
    return dir(obj)
