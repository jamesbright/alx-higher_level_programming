#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    new_list = my_list.reverse()

    for value in len(new_list):
        print("{:d}".format(value))
