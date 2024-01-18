#!/usr/bin/python3
"""
single character H
Calculate least number of operations needed
to result in n number of H characters
if n <=1 return o
returns an integer
"""


def minOperations(n: int) -> int:
    """
    calculate least number of operations
    """
    if n <= 1:
        return 0

    num_of_operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            num_of_operations = num_of_operations + divisor
            n = n // divisor
        divisor = divisor + 1

    return num_of_operations
