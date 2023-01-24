#!/bin/usr/python3

def safe_print_division(a, b):
    res = None
    try:
        res = a / b
    except Exception as e:
        raise
    finally:
        print("Inside Result:{:d}".format(res))

    return res
