#!/usr/bin/env python3
"""checking if all locked boxes can be opened or not"""


def canUnlockAll(boxes):
    """returns true if openable or false if not"""
    if not boxes or not boxes[0]:
        return False
    
    n = len(boxes)
    visited =[False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key > n and not visited[key]:
                visited[key] = True
                stack.append(key)

    if all(visited):
        return True
    return False
