#!/usr/bin/python3
"""
method that determines if all the boxes can be opened.
n is number of locked boxes and numbered sequentially from 0 to n - 1
Each box may contain keys to the other boxes.
boxes is a list of lists
A key with the same number as a box opens that box
Assume all keys will be positive integers
    -    There can be keys that do not have boxes
    -    The first box boxes[0] is unlocked
 Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """

    """
    number = len(boxes)
    boxes_visited = set()
    keys = [0]

    boxes_visited.add(0)

    while keys:
        box_index = keys.pop()
        for key in boxes[box_index]:
            if key < number and key not in boxes_visited:
                boxes_visited.add(key)
                keys.append(key)
    return len(boxes_visited) == number
