#!/usr/bin/env python3
""" This function adds the values of two arrays together.
    This only works if both arrays are the same size. Otherwise an out of bounds
    error will occur
"""


def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None

    new_array = []
    for i in range(len(arr1)):
        new_array.append(arr1[i] + arr2[i])

    return new_array
