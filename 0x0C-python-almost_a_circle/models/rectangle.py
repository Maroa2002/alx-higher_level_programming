#!/usr/bin/python3
"""
model: rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor
        width: Width of the rectangle.
        height: Height of the rectangle.
        x (defaulting to 0): x-coordinate of the rectangle.
        y (defaulting to 0): y-coordinate of the rectangle.
        id (defaulting to None): An optional identifier for the rectangle.
        """
        # Call the super class with id
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """returns the area value"""
        return (self.__height * self.__width)

    def display(self):
        """prints the Rectangle instance with the character #"""
        for _ in range(self.__y):
            # vertical offset - y-coordinate
            print()

        for _ in range(self.__height):
            # horizontal offset - x-coordinate
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        """returns string representation of an obeject"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        # attribute_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                # iterating while keeping track of the index
                # for index, item in enumerate(iterable):
                # if i < len(attribute_list):
                #     setattr(self, attribute_list[i], args[i])
                # else:
                #     break
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                else:
                    self.y == arg
        elif kwargs:
            # for key, value in kwargs.items():
            #     if key in attribute_list:
            #         setattr(self, key, value)
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        # rectangle_dict = {}
        # rectangle_dict["id"] = self.id
        # rectangle_dict["width"] = self.width
        # rectangle_dict["height"] = self.height
        # rectangle_dict["x"] = self.x
        # rectangle_dict["y"] = self.y
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
