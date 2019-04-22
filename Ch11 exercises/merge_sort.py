def merge(lyst, copybuffer, low, middle, high):
    # lyst          liist being sorted
    # copybuffer    temp space needed during the merge
    # low           beginning of the first sorted sublist
    # middle        end of the first sorted sublist
    # middle + 1    beginning of the second sorted sublist
    # high          end of the second sorted sublist

    # Initialize i1 and i2 to the first items in each sublist
    i1 = low
    i2 = middle + 1

    # Interleave items from the sublists into the
    # copybuffer in such a way that order is maintained.
    for i in range(low, high + 1):
        if i1 > middle:
            copybuffer[i] = lyst[i2]  # First sublist exhausted
            i2 += 1
        elif i2 > high:
            copybuffer[i] = lyst[i1]  # Second sublist exhausted
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            copybuffer[i] = lyst[i1]  # Item in first sublist is <
            i1 += 1
        else:
            copybuffer[i] = lyst[i2]  # Item in second sublist is <
            i2 += 1

    for i in range(low, high + 1):
        lyst[i] = copybuffer[i]


def mergeSortHelper(lyst, copybuffer, low, high):
    # lyst          liist being sorted
    # copybuffer    temp space needed during the merge
    # low, high     boundaries of the sublist
    # middle        midpoint of the list
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst, copybuffer, low, middle)
        mergeSortHelper(lyst, copybuffer, middle + 1, high)
        merge(lyst, copybuffer, low, middle, high)


def mergeSort(lyst):
    # lyst          the list being sorted
    # copybuffer    temp space needed during the merge
    copybuffer = list(lyst)
    mergeSortHelper(lyst, copybuffer, 0, len(lyst) - 1)

import random

def main(size = 10, sort = mergeSort):
    """Sort a randomly ordered list and print
    before and after."""
    lyst = list(range(1, size + 1))
    random.shuffle(lyst)
    print(lyst)
    sort(lyst)
    print(lyst)

if __name__ == "__main__":
    main()
