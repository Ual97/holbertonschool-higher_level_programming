#!/usr/bin/python3
"""
Module 1-square
defines class square with private attribute size
"""


class Square:
    """
    class square definiton

    Args:
        size: size of square
    """
    def __init__(self, size):
        """
        initializes square

        Attributes:
            size: size of square
        """
        self.__size = size
