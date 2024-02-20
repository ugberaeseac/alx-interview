#!/usr/bin/python3
"""
Rotate a 2-D matrix 90 degrees clockwise(Transpose)
Matrix must be edited in-place
Matrix can be assumed to not be empty
"""


def rotate_2d_matrix(matrix):
    """
    rotate the 2-dimensional matrix
    """
    if matrix == []:
        return
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
