#!/usr/bin/python3
"""Square class and functions"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes size"""
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
