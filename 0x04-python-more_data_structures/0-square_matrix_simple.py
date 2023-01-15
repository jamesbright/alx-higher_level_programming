#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """finds the squares of all elements
    of a matrix"""
    value = []

    for row in matrix:
        square = map(lambda el: el**2, row)
    
    value.append(list(square))

    return (value)
