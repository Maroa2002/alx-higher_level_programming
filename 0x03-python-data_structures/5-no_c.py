#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None and len(my_string) != 0:
        for char in my_string:
            if char == 'c' or char == 'C':
                my_string = my_string.replace(char, '')
        return my_string
