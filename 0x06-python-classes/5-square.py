#!/usr/bin/python3
"""Square class and methods that returns area"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes size"""
        self.__size = size

    def area(self):
        """function returns area data
        Returns:
            area: area data
        """
        return self.__size**2

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """prints size with # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
