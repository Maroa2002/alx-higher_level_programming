#!/usr/bin/python3
"""
contains the function class_to_json
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    if isinstance(obj, (int, bool, str)):
        # return object itself if a basic data type
        return obj
    elif isinstance(obj, list):
        # simplify each element if object is a list
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        # simplify keys and values if a dictionary
        return {str(key): class_to_json(value) for key, value in obj.items()}
    else:
        # convert to string representation for unknown type
        return str(obj)
