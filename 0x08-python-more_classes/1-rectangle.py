#!/usr/bin/python3
"""Rectangle class and methods"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialise Objects"""
        this.__width = width
        this.__height = height

    @property
    def width(self):
        """Get width property"""
        return self.width

    @property.setter
    def width(self, value):
        """Set width property"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise valueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """Get height property"""
        return self.height

    @property.setter
    def height(self, value):
        """Set height property"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise valueError("height must be >= 0")
        self.height = value
