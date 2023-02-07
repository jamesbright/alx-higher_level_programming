#!/usr/bin/python3
"""
Line function
"""


def number_of_lines(filename=""):
    """number of lines from file
    args:
        filename: file to read
    return:
        number of lines
    """
    with open(filename, "r", encoding="UTF-8") as f:
        return len(list(f))
