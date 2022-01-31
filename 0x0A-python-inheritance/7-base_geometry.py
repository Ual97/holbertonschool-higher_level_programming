#!/usr/bin/python3
"""
Module 7-base_geometry

methods:
     def area(self):
        raises exception message
    def integer_validator(self, name, value):
        validates value and raises error accordingly
"""


class BaseGeometry:
    """
    Method area(self)
    """
    def area(self):
        """raise exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
