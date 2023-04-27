#!/usr/bin/python3
""" Finds the peak of a list
"""


def divide_conquer(arr, low, high):
    """ uses divide and conquer algorithm
    """

    mid = int((low + high) / 2)
    if arr[mid-1] <= arr[mid] and arr[mid] >= arr[mid+1]:
        return arr[mid]
    elif arr[mid] > arr[mid+1]:
        return divide_conquer(arr, low, mid-1)
    elif arr[mid] < arr[mid+1]:
        return divide_conquer(arr, mid+1, high)


def find_peak(list_of_integers):
    """ find list peak
    """

    if not list_of_integers:
        return None
    return divide_conquer(list_of_integers, 0, len(list_of_integers)-1)
