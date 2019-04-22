"""
testsort test for a list to be in ascending order
Uses both iterative and recursive approaches
Author: Dave
"""

def isSorted(lyst):
    """Loop through the list to find the first element out of order"""
    if len(lyst) < 2:
        return True
    else:
        for i in range(len(lyst) - 1):
            if lyst[i] > lyst[i + 1]:
                return False
        return True

def is_sorted(lyst):
    """Recurse through the list to find the first element out of order"""
    if len(lyst) < 2:
        return True
    elif lyst[0] > lyst[1]:
        return False
    else:
        return is_sorted(lyst[1:len(lyst)])

def main():
    lyst = []
    assert(isSorted([lyst]) == True)
    print(isSorted(lyst))
    lyst = [1]
    assert(isSorted([lyst]) == True)
    print(isSorted(lyst))
    lyst = list(range(10))
    assert(isSorted([lyst]) == True)
    print(isSorted(lyst))
    lyst[9] = 3
#    assert(isSorted([lyst]) == False)
    print(isSorted(lyst))

    lyst = []
    assert(is_sorted([lyst]) == True)
    print(is_sorted(lyst))
    lyst = [1]
    assert(is_sorted([lyst]) == True)
    print(is_sorted(lyst))
    lyst = list(range(10))
    assert(is_sorted([lyst]) == True)
    print(is_sorted(lyst))
    lyst[9] = 3
#    assert(is_sorted([lyst]) == False)
    print(is_sorted(lyst))

if __name__ == '__main__':
    main()