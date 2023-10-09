#!/usr/bin/python3
"""
contains the method is_same_class
"""


def is_same_class(obj, a_class):
    """checks for an instance of an object"""
    return type(obj) is a_class
