#!/usr/bin/python3
"""
Log parsing
script that reads stdin line by line and computes metrics
"""


import sys
import signal


total_file_size = 0
status_code_count = {}


def print_stat():
    """
    print statistics
    """
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_count.keys()):
        print("{}: {}".format(
            status_code, status_code_count[status_code]))


def sig_handler(signal, handler):
    """
    Handle kyboard interruption signmal
    """
    print_stat()
    sys.exit(0)


signal.signal(signal.SIGINT, sig_handler)


try:
    for line_num, line in enumerate(sys.stdin, start=1):
        try:
            parse_line = line.split()
            if len(parse_line) >= 10 and parse_line[5].isdigit():
                file_size = int(parse_line[9])
                status_code = int(parse_line[8])

                total_file_size = total_file_size + file_size
                status_code_count[status_code] = status_code_count.get(
                        status_code, 0) + 1

            if line_num % 10 == 0:
                print_stat()

        except (IndexError, ValueError):
            pass
except KeyboardInterrupt:
    print_stat()
    sys.exit(0)
