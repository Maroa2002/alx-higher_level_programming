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

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the square with # character"""
        if self.__size is 0:
            print("")
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print()
