#!/usr/bin/python3
"""
Module 3-square
defines class square with private attribute size
"""


from sunau import Au_read


class Square:
    """
    class square definiton

    Args:
        size: size of square
    Functions:
        __init__(self, size=0)
        area(self)
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

    def area(self):
        """
        area of square

        Returns:
            area of square
         """
        return(self.__size)**2
