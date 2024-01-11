#!/usr/bin/env python3
"""checking if all locked boxes can be opened or not"""


def canUnlockAll(boxes):
    """returns true if openable or false if not"""
    if not boxes or not boxes[0]:
        return False
    acc = 0

    for i in range(1, len(boxes)):
        for j in range(0, len(boxes)):
            if i in boxes[j] and i != j:
                acc += 1
                break

    if acc == (len(boxes) - 1):
        return True
    return False
