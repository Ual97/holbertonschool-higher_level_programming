#!/usr/bin/python3
"""
Module 8-rectangle
Contains parent class BaseGeometry
with public instance method area and integer_validator
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """validate and initialize width and height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
