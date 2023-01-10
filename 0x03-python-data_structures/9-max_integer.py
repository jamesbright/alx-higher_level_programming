#!/usr/bin/python3

def max_integer(my_list=[]):
    if not len(my_list):
        return None
    else:
        for i in range(1, len(my_list)):
            if my_list[i - 1] > my_list[i]:
                max_num = my_list[i-1]
            else:
                max_num = my_list[i]

        return (max_num)
