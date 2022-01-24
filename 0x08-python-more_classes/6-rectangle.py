#!/usr/bin/python3
"""
Module 4-Rectangle
Defines an empty class Rectangle
"""


class Rectangle:
    """Rectangle Class

        Args:
            width: width of rectangle

            height: height of rectangle
    """
    num_of_instances = 0

    def __init__(self, width=0, height=0):
        """init Rectangle"""
        self.width = width
        self.height = height
        type(self).num_of_instances += 1

    def __del__(self):
        """Deletes instance"""
        print("Bye rectangle...")
        type(self).num_of_instances -= 1

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width if > 0 and if int"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height if > 0 and if int"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Prints the rectangle
            Returns:
                rectangle in #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            pr = "\n".join(["#" * self.__width for r in range(self.__height)])
            return pr

    def __repr__(self):
        """str repr, recreates a new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
