#!/usr/bin/python3
"""
contains the append_write function
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)
    return:
            the number of characters added:
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
