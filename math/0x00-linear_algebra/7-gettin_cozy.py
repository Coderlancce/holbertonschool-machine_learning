#!/usr/bin/env python3
"""That concatenates two matrices along a specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concat 2d matrix a specific axis
    """
    if (len(mat1[0]) == len(mat2[0])) and (axis == 0):
        new_matrix = [num.copy() for num in mat1]
        new_matrix += [num.copy() for num in mat2]
        return new_matrix
    elif (len(mat1) == len(mat2)) and (axis == 1):
        new_matrix = [mat1[aux] + mat2[aux] for aux in range(len(mat1))]
        return new_matrix
    else:
        return None
