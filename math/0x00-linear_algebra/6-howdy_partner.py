#!/usr/bin/env python3
""" That concatenates two arrays
"""


def cat_arrays(arr1, arr2):
    """ Add elements to new array
    """
    new_matrix = arr1.copy()
    for i in arr2:
        new_matrix.append(i)
    return new_matrix
