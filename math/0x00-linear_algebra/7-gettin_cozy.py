#!/usr/bin/env python3
"""
    This function concatenates two matrices. Unlike 6-howdy_partner,
    the passed in axis determines how the matrices are being concatenated
    If axis is 0, concatenate the matrices such that the number
    of columns are preserved
    If axis is 1, concatenate the matrices such that the number
    of rows are preserved
"""


def cat_matrices2D(mat1, mat2, axis=0):
    new_matrix = mat1.copy()
    
    if axis is 0:
        new_matrix = mat1 + mat2
    else:
        for i in range(len(new_matrix)):
            new_matrix[i].append(mat2[i][0])
    
    return new_matrix
