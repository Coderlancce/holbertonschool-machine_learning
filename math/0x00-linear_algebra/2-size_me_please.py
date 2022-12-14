#!/usr/bin/env python3
"""That calculates the shape of a matrix
"""


def matrix_shape(matrix):
    """Recursive function to count in a list the size
    """
    if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])
