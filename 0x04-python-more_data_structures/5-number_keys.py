#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    a function that returns the number of keys in a dictionary
    """
    if a_dictionary is not None:
        count = 0
        for key in a_dictionary:
            count += 1
        return count
