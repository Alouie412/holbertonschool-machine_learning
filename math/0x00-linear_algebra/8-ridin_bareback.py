#!/usr/bin/env python3
""" This function performs matrix multiplication """


def mat_mul(mat1, mat2):
    """
    Here, mat2[0] is our width, and mat1 is our height.
    This is needed to initialize our resulting matrix
    """
    new_matrix = [[0 for j in range(len(mat2[0]))] for i in range(len(mat1))]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                try:
                    new_matrix[i][j] += mat1[i][k] * mat2[k][j]
                except:
                    return None

    return new_matrix
