#!/usr/bin/python3
"""a function for validating a given set of data according to utf-8"""


def validUTF8(data):
    """UTF-8 validation"""
    # Variable to keep track of remaining bytes for a multi-byte character
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if (byte >> 5) == 0b110 or (byte >> 5) == 0b1110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7) != 0:
                # Invalid starting byte
                return False
        else:
            # Check if the byte is a continuation byte
            if (byte >> 6) != 0b10:
                # Invalid continuation byte
                return False
            num_bytes -= 1

    # Check if there are any remaining bytes
    return num_bytes == 0
