#!/usr/bin/env python3
""" Adds two arrays element-wise
"""


def add_arrays(arr1, arr2):
    """ Create a new array with the sum and return
    """
    if len(arr1) != len(arr2):
        return None
    new_array = []
    return [(arr1[i] + arr2[i]) for i in range(len(arr1))]
