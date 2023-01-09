#!/usr/bin/python3

def no_c(my_string):
    """Removes all c and C
    in a string
    """
    new_string = ""
    for index in range(len(my_string)):
        if my_string[index] != "c" and my_string[index] != "C":
            new_string += my_string[index]

    return (new_string)
