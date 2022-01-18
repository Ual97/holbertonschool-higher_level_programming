#!/usr/bin/python3
"""
Module 2-square
defines class square with private attribute size
"""


class Square:
    """
    class square definiton

    Args:
        size: size of square
    """
    def __init__(self, size=0):
        """
        initializes square

        Attributes:
            __size (int): size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
