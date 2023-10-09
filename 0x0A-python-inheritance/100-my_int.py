#!/usr/bin/python3
"""
contains class MyInt
"""


class MyInt(int):
    """A class that inherits from int"""
    def __eq__(self, num):
        """equal"""
        return (int(self) != num)

    def __ne__(self, num):
        """no equal"""
        return (int(self) == num)
