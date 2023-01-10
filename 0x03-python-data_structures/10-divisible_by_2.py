#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not len(my_list):
        return None
    else:
        divisible = map(lambda x: x % 2 == 0, my_list)
        divisible = list(divisible)
        return divisible
