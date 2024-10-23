#!/usr/bin/python3
""" 0-stats.py - Reads stdin line by line and computes metrics """

import sys
import signal

def print_stats(total_size, status_codes):
    """ Print accumulated metrics """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def signal_handler(sig, frame):
    """ Handle CTRL + C """
    print_stats(total_size, status_codes)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 9:
            continue

        try:
            ip = parts[0]
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

        except ValueError:
            continue

        line_count += 1
        if line_count == 10:
            print_stats(total_size, status_codes)
            line_count = 0

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

# Ensure printing the final stats even if the loop ends naturally
print_stats(total_size, status_codes)
