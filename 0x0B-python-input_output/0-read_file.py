#!/usr/bin/python3
"""
contains the read_file function
"""


def read_file(filename=""):
    """reads file and prints to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        data_read = file.read()
        print(data_read, end="")
