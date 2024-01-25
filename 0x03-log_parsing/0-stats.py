#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
from collections import defaultdict


def compute_metrics(lines, total_size=0):
    """compute metrics"""
    status_code_count = defaultdict(int)

    for line in lines:
        try:
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            # print(parts)
            # Check if the line follows the specified format
            if (
                parts[4] == '"GET' and
                parts[5].startswith("/projects/") and
                parts[6] == 'HTTP/1.1"'
            ):
                total_size += file_size
                status_code_count[status_code] += 1

        except (ValueError, IndexError):
            # Skip lines that don't match the expected format
            continue

    return total_size, status_code_count


def print_metrics(total_size, status_code_count):
    """print metrics"""
    print(f"File size: {total_size}")

    for code in sorted(status_code_count):
        print(f"{code}: {status_code_count[code]}")


def main():
    """main function for handling everything"""
    lines = []
    try:
        total_size = 0
        for line in sys.stdin:
            lines.append(line.strip())
            if len(lines) == 10:
                total_size, status_code_count = compute_metrics(lines,
                                                                total_size)
                print_metrics(total_size, status_code_count)
                lines = []

    except KeyboardInterrupt:
        total_size, status_code_count = compute_metrics(lines, total_size)
        print_metrics(total_size, status_code_count)


if __name__ == "__main__":
    main()
