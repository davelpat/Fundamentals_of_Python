"""
File: testquicksort.py

Tests the quicksort algorithm
"""

def quicksort(lyst):
    """Sorts the items in lyst in ascending order."""
    quicksortHelper(lyst, 0, len(lyst) - 1)

def quicksortHelper(lyst, left, right):
    """Partition lyst, then sort the left segment and
    sort the right segment."""
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
    """Shifts items less than the pivot to its left,
    and items greater than the pivot to its right,
    and returns the position of the pivot."""
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = swap(lyst, middle, right)
    # pivot = lyst[middle]
    # lyst[middle] = lyst[right]
    # lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap(lyst, right, boundary)
    return boundary

    quicksortHelper(0, len(lyst) - 1)

def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
    return temp

import random

def main(size = 20, sort = quicksort):
    """Sort a randomly ordered list and print
    before and after."""
    lyst = list(range(1, size + 1))
    random.shuffle(lyst)
    print(lyst)
    sort(lyst)
    print(lyst)

if __name__ == "__main__":
    main() 
