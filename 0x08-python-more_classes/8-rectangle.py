#!/usr/bin/python3
"""Rectangle class and methods with attribute width and height"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise Objects"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """called when a rectangle object is removed"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares rectangle objexts"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):
        total = ""
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    total += str(self.print_symbol)
                except Exception:
                    total += type(self).print_symbol
            if i is not self.__height - 1:
                total += "\n"
        return total

    def area(self):
        """Calculate and return area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate and return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

