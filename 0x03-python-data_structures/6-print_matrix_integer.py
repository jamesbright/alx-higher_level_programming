#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints elements of a 
    matrix
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print("{:d}".format(matrix[row][col]))
