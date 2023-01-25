#!/usr/bin/python3
"""Square class and methods that returns area"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes size and position"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter"""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Setter"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 integers")
        if any(type(i) != int for i in value or any(j < 0 for j in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints size with # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()

