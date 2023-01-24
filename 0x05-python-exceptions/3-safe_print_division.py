#!/usr/bin/python3

def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside Result: {:d}".format(res))
        return res

    return
