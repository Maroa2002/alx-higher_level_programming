#!/usr/bin/python3
"""
contains class square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """derived class"""
    def __init__(self, size):
        """constructor"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
