#!/usr/bin/env python3
"""
Calculates a sigma
"""


def summation_i_squared(n):
    """
    Need a limit for the sigma function
    """
    if (type(n) is not int) or (n is None) or (n < 1):
        return None

    else:
        limit = range(1, n + 1)
        sigma = 0
        sigma = map(lambda i: i ** 2, limit)
        return sum(sigma)
