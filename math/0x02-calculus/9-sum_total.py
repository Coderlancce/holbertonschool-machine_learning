#!/usr/bin/env python3
"""
Calculates a sigma
"""


def summation_i_squared(n):
    """
    Need a limit for the sigma function
    """
    i = 1
    sum = 0

    if (type(n) is not int) or (n is None) or (n < 1):
        return None

    while (i != n + 1):
        sum = sum + i**2
        i += 1

    return sum
