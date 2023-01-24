#!/usr/bin/pythoin3

def safe_print_list(my_list=[], x=0):
    """Prints a list and hanles exception
    with try and catch"""
    counter = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except Exception as e:
            break
        else:
            counter += 1
    print()
    return counter
