#!/usr/bin/python3
"""generating pascal's triangle up to certain number of rows"""


def pascal_triangle(n):
    """a function for generating pascal's triangle
    params:
    n: num of rows to generated
    Return: a list of lists of integers of pascal's triangle
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
