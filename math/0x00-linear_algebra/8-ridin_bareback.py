#!/usr/bin/env python3
"""That performs matrix multiplication
"""


def mat_mul(mat1, mat2):
    """ Create a matrix with multiplcation result
    """
    if len(mat1[0]) == len(mat2):
        new_matrix = []
        for row_a in range(len(mat1)):
            inner = []
            for col_b in range(len(mat2[0])):
                number = 0
                for col_a in range(len(mat1[0])):
                    number += (mat1[row_a][col_a] * mat2[col_a][col_b])
                inner.append(number)
            new_matrix.append(inner)
        return new_matrix
    else:
        return None
