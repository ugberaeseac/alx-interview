#!/usr/bin/python3
"""
Log parsing
script that reads stdin line by line and computes metrics
"""


import sys


total_file_size = 0
status_code_count = {}


def print_stat(total_file_size, status_code_count):
    """
    print statistics
    """
    print("File size: {:d}".format(total_file_size))
    for status_code in sorted(status_code_count.keys()):
        print("{:d}: {:d}".format(
            status_code, status_code_count[status_code]))


try:
    for line_num, line in enumerate(sys.stdin, start=1):
        try:
            parse_line = line.split()
            file_size = int(parse_line[-1])
            status_code = int(parse_line[-2])

            total_file_size = total_file_size + file_size
            status_code_count[status_code] = status_code_count.get(
                    status_code, 0) + 1

            if line_num != 0 and line_num % 10 == 0:
                print_stat(total_file_size, status_code_count)

        except (IndexError, ValueError):
            pass
    print_stat(total_file_size, status_code_count)
except KeyboardInterrupt:
    print_stat(total_file_size, status_code_count)
    raise
