#!/usr/bin/python3
"""

"""


class MyInt(int):
    """A class that inherits from int"""
    def __eq__(self, num):
        """ """
        return (int(self) != num)

    def __ne__(self, num):
        """ """
        return (int(self) == num)