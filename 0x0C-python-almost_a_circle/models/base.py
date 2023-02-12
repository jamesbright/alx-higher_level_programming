#!/usr/bin/python3
""" Base class """


class Base:
    """ base class with some methods"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize class members """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
