#!/usr/bin/python3
"""Module to validate UTF-8 encoding"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing byte data
    :return: True if data is a valid UTF-8 encoding, else False
    """
    number_of_bytes = 0

    for num in data:
        binary_rep = format(num, '#010b')[-8:]

        if number_of_bytes == 0:
            for bit in binary_rep:
                if bit == '0':
                    break
                number_of_bytes += 1

            if number_of_bytes == 0:
                continue

            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (binary_rep[0] == '1' and binary_rep[1] == '0'):
                return False

        number_of_bytes -= 1

    return number_of_bytes == 0
