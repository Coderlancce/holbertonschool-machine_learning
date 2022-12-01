#!/usr/bin/env python3
"""That returns the transpose of a 2D matrix, matrix
"""


def matrix_transpose(matrix):
    """check all positions and transpose
    """
    new_matrix = []
    for row in range(len(matrix[0])):
        new_matrix.append([matrix[col][row] for col in range(len(matrix))])
    return new_matrix
