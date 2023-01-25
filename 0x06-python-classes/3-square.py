#!/usr/bin/python3
"""Square class and functions that returns area"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes size"""
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """function returns area data
        Returns:
            area: area data
        """
        return self.__size**2
