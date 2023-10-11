#!/usr/bin/python3
"""
contains the function class_to_json
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
