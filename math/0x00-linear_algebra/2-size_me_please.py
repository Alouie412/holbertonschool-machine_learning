#!/usr/bin/env python3
"""
    This function calculates and returns the size of a matrix
    Try/except is used to circumvent a TypeError when appending
"""


def matrix_shape(matrix):
    new_matrix = []

    try:
        new_matrix.append(len(matrix))
        new_matrix.append(len(matrix[0]))
        new_matrix.append(len(matrix[0][0]))
    except:
        pass

    return new_matrix
