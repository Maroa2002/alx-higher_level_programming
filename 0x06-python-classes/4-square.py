#!/usr/bin/python3
"""
module: 2-square
defines a class Square
"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getter function to retrieve __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function to set the __size"""
        self.__size = value

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)
