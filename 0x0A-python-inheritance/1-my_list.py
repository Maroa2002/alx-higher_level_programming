#!/usr/bin/python3
"""
contains the method MyList
"""


class MyList(list):
    """prints sorted list in ascending order """
    def print_sorted(self):
        print(sorted(self))
