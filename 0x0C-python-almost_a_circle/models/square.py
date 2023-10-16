#!/usr/bin/python3
"""
model: square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class contructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.width = value

    def __str__(self):
        """returns string representation of objects"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y == arg
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        square_dict = {}
        square_dict["id"] = self.id
        square_dict["x"] = self.x
        square_dict["size"] = self.size
        square_dict["y"] = self.y
        return square_dict
