#!/usr/bin/python3
"""
model: base
"""


class Base:
    """Base  of all other classes in the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
