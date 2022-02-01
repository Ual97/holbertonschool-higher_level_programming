#!/usr/bin/python3
"""
Module 8-rectangle

inherits from BaseGeometry
instantiation of private attributes width and height
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """based on parent class BaseGeometry"""
    def __init__(self, width, height):
        """init with width and heigth"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
