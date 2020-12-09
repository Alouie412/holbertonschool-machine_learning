#!/usr/bin/env python3
"""
    This function concatenates two matrices along a specific axis,
    using numpy
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    return np.concatenate((mat1, mat2), axis=axis)
