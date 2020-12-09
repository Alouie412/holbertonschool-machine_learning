#!/usr/bin/env python3
"""
    This function adds two matrices of the same shape.
    If this is not possible, return None
"""


def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    new_matrix = mat1[:]
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            new_matrix[i][j] = mat1[i][j] + mat2[i][j]

    return new_matrix
