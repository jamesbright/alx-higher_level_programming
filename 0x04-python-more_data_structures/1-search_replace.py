#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """finds and replaces a value in a list"""
    value  = [num if num != search else replace for num in my_list]
    return value

