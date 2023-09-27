#!/usr/bin/python3
"""
module: 2-square
defines a class Square
"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for setting position"""
        if not isinstance(value, tuple) or len(value) != 2 \
            or not all(isinstance(i, int) for i in value) \
                or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the square with # character"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
