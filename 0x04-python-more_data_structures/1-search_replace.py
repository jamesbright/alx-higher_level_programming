#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """finds and replaces a value in a list"""
    for index in range(len(my_list)):
        if search == my_list[index]:
            my_list[index] = replace
            

    return (my_list)

