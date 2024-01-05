#!/usr/bin/python3
"""
function that returns a list of lists of integers
representing the Pascal’s triangle of n

assumes n will always be an integer
Returns an empty list if n <= 0
"""


def pascal_triangle(n):
    """
    pascal triangle
    return a list of lists of integers
    """
    triangle_list = []

    if n <= 0:
        return []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle_list[i - 1][j - 1] + triangle_list[i - 1][j]
        triangle_list.append(row)

    return triangle_list
