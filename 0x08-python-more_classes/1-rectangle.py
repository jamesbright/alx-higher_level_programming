#!/usr/bin/python3
"""Rectangle class and methods with attribute width and height"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialise Objects"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width property"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height property"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
