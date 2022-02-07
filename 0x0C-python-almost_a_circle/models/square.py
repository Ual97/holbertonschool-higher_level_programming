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

    def update(self, *args, **kwargs):
        """assings an argument to each attribute in the
        following order:
            1 - id
            2 - size
            3 - x
            4 - y
        """
        if args is not None and len(args) != 0:
            attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attr[i], args[i])

        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
