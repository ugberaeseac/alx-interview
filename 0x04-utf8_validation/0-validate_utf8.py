#!/usr/bin/python3
"""
represents a valid UTF-8 encoding
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data
Return: True if data is a valid UTF-8 encoding, else return False
"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    checks if a given data set represents
    a valid UTF-8 encoding
    """

    num_bytes_to_check = 0

    for byte in data:
        if num_bytes_to_check == 0:
            if byte & 0b10000000 == 0:
                num_bytes_to_check = 1
            elif byte & 0b11100000 == 0b11000000:
                num_bytes_to_check = 2
            elif byte & 0b11110000 == 0b11100000:
                num_bytes_to_check = 3
            elif byte & 0b11111000 == 0b11110000:
                num_bytes_to_check = 4
            else:
                return False
        else:
            if byte & 0b11000000 != 0b10000000:
                return False

        num_bytes_to_check = num_bytes_to_check - 1

        if num_bytes_to_check < 0:
            return False

    return num_bytes_to_check == 0
