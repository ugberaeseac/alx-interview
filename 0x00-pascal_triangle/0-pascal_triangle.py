#!/usr/bin/python3
"""
function that returns a list of lists of integers
representing the Pascal’s triangle of n

assumes n will be always an integer
Returns an empty list if n <= 0
"""


from math import factorial


def pascal_triangle(n):
    """
    pascal triangle
    return a list of lists of integers
    """
    triangle_list = []

    if n >= 0:
        for i in range(n):
            row = []
            for j in range(i + 1):
                value = (factorial(i) // (factorial(j) * factorial(i - j)))
                row.append(value)
            triangle_list.append(row)
        return triangle_list
    else:
        return "[]"
