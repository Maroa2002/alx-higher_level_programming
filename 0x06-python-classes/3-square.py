#!/usr/bin/python3
"""
module: 2-square
defines a class Square
"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)
