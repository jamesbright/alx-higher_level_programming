#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints elements of a 
    matrix
    """
    if not matrix:
        print()
    else:
        
        for row in matrix:
            for col in row:
                print("{:d}".format(col), end=' ' if col != row[-1] else '\n')
