#!/usr/bin/python3
"""
Module-0-add_integer
Takes 2 values and returns the sum of them,
if a float value is passed it is converted to int
"""


def add_integer(a, b=98):
    """
    Returns sum of a + b as int, raises error if not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
