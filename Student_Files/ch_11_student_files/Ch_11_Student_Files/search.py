"""
File: search.py

Defines functions for sequential search and binary search with a profiler.
"""

def sequentialSearch(target, lyst, profiler = None):
    """Returns the position of the target item if found,
    or -1 otherwise."""
    position = 0
    while position < len(lyst):
        if profiler: profiler.comparison()
        if target == lyst[position]:
            return position
        position += 1
    return -1

def binarySearch(target, lyst, profiler = None):
    """Returns the position of the target item if found,
    or -1 otherwise."""
    left = 0
    right = len(lyst) - 1
    while left <= right:
        if profiler: profiler.comparison()
        midpoint = (left + right) // 2
        if target == lyst[midpoint]:
            return midpoint
        elif target < lyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1


