#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None and len(my_string) != 0:
        new_string = ""
        for char in my_string:
            if char != 'c' and char != 'C':
                new_string += char
        return new_string
