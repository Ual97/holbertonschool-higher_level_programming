#!/usr/bin/python3
"""
Module 9-rectangle

adds print and str functions to class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """validate and initialize width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
