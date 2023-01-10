#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        exit (1)
    else:
        for i in range(1, len(my_list)):
            if my_list[i - 1] > my_list[i]:
                max_num = my_list[i-1]
            else:
                max_num = my_list[i]

        return (max_num)
