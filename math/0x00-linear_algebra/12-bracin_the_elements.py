#!/usr/bin/env python3
"""
    This function performs element-wise addition, subtraction, multiplication, and
    division. The results are returned as a tuple
"""


def np_elementwise(mat1, mat2):
    return (mat1 + mat2), (mat1 - mat2), (mat1 * mat2), (mat1 / mat2)
