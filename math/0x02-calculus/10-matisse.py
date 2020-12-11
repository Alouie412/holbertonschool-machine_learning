#!/usr/bin/env python3
"""
This script takes an equation in list form and returns the
derivative in list form. Only the coefficients are returned,
as the variable and power are assumed to be understood
"""

def poly_derivative(poly):
    """ Calculate the derivative of the list """
    if poly is None:
        return None

    new_poly = []
    iterater = 0
    for i in poly:
        new_poly.append(i * iterater)
        iterater = iterater + 1

    """ Popping the first entry in the list is needed,
    as the derivative of a constant is 0 """
    new_poly.pop(0)
    return new_poly
