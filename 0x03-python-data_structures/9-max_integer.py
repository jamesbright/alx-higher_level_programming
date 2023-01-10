#!/usr/bin/python3

def max_integer(my_list=[]):
    if not len(my_list):
        return None
    else:
        max_num = my_list[0]
        for item in my_list:
            if i <= item:
                max_num = max_num
            else:
                max_num = item

        return (max_num)
