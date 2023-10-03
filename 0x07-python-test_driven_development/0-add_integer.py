#!/usr/bin/python3
"""contains a methos that adds 2 integers
    Args: a = first value
          b = second value
    return: an integer: the addition of a and b
    raise: TypeError exception if a or b is not int or float"""


def add_integer(a, b=98):
    """
    returns the integer sum of values a and b
    """
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return a + b
