#!/usr/bin/python3
"""
contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
args: text - input text
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters:., ? and :
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    # result = []
    # current_line = ''

    # for c in text:
    #     current_line += c
    #     if c in ".?:":
    #         result.append(current_line.strip())
    #         current_line = ''

    # if current_line.strip():
    #     result.append(current_line.strip())

    # print('\n\n'.join(result))
    for c in ".:?":
        text = (c + "\n\n").join(
            [line.strip(" ") for line in text.split(c)])

    print(text, end="")
