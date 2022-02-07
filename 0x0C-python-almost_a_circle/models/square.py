#!/usr/bin/python3
"""
Square class (inherits from rectangle):
    attributes:
        width (size)
        height (size)
        x
        y
    class constructor:
        def __init__(self, size, x=0, y=0, id=None):
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init square class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    @property
    def size(self):
        """Getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size"""
        self.width = value
        self.height = value
