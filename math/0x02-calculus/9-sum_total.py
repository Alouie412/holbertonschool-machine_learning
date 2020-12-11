#!/usr/bin/env python3
"""
This script returns a summation of n squared.
Loops are not allowed, thus an alternative is necessary, which is to
utilize a certain equation mathematicians of old have found
"""

def summation_i_squared(n):
    """ Calculate the sum of n squared """
    if not isinstance(n, int):
        return None

    total = (n * (n + 1) *
            (2 * n + 1 )) // 6

    return total
