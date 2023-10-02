#!/usr/bin/python3
"""
module: 0-rectangle
contains the class Rectangle
Rectangle has the attributes width and height
"""


class Rectangle:
    """
    defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes the rectangles fields"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter that retrives the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter that sets width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """getter that retrives the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter that sets height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """returns rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """prints the rectanglw with #s"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rect_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += str(self.print_symbol)
            rect_str += '\n'
        return rect_str[:-1]

    def __repr__(self):
        """returns a string representation of a rectangle"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """deletes an instane of rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
