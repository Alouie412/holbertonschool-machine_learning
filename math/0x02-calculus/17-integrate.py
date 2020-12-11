#!/usr/bin/env python3
"""
This script takes an equation in list form and returns the
indefinite integral in list form. Only the coefficients are
returned, as the variable and power are assumed to be understood
Furthermore, if a coefficient is a whole number, it is displayed
as an int. Otherwise it is displayed as a float
"""

def poly_integral(poly, C=0):
    """ Calculate the indefinite integral of an equation """
    if poly is None:
        return None

    if not isinstance(C, int):
        return None

    new_poly = []
    new_poly.append(C)

    iterator = 1
    for i in poly:
        if i % iterator == 0:
            new_poly.append(i // iterator)
        else:
            new_poly.append(i / iterator)
        
        iterator = iterator + 1

    return new_poly
