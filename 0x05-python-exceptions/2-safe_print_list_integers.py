#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    for item in range(0, x):
        try:
            print("{:d}".format(my_list[item], end=""))
        except IndexError:
            raise
        except Exception as e:
            pass
        else:
            counter += 1

    print()
    return counter
