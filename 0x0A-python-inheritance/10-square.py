#!/usr/bin/python3
"""
Module 10-square
has area implemented, size must be private and positive integer
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle
    """
    def __init__(self, size):
        """initializes size
        """
        self.integer_validator("size", size)
        self.__init__(size, size)
        self.__size = size
