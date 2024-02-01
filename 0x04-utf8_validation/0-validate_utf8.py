#!/usr/bin/python3
"""a function for validating a given set of data according to utf-8"""


def validUTF8(data):
    """UTF-8 validation"""
    # Variable to keep track of remaining bytes for a multi-byte character
    remaining_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte (starts with '10')
        if remaining_bytes > 0 and (byte >> 6) == 0b10:
            remaining_bytes -= 1
        elif (byte >> 7) == 0:
            # Single-byte character (starts with '0')
            remaining_bytes = 0
        elif (byte >> 5) == 0b110:
            # Two-byte character (starts with '110')
            remaining_bytes = 1
        elif (byte >> 4) == 0b1110:
            # Three-byte character (starts with '1110')
            remaining_bytes = 2
        elif (byte >> 3) == 0b11110:
            # Four-byte character (starts with '11110')
            remaining_bytes = 3
        else:
            # Invalid starting byte
            return False

    # Check if there are remaining bytes after iterating through the entire data
    return remaining_bytes == 0
