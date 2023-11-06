#!/usr/bin/python3
'''
Write a method that determines if all the boxes can be opened.
    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
'''


def canUnlockAll(boxes):
    key = [0]
    for k in key:
        for i in boxes[k]:
            if i not in key and i < len(boxes):
                key.append(i)
    if len(key) == len(boxes):
        return True
    else:
        return False
