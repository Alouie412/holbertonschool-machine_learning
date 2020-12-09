#!/usr/bin/env python3
"""
    This function transposes a 2D Matrix.
    In other words, flips the matrix by 90 degrees
"""


def matrix_transpose(matrix):
    """
    Loop and iterate through i, loop and iterate through j,
    and set matrix[j][i] to new_matrix
    """
    new_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    return new_matrix
