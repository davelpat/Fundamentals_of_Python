"""
Instructions for programming Exercise 5.1

A group of statisticians at a local college has asked you to create a set of
functions that compute the median and mode of a set of numbers. Define these
functions, median and mode, in a module named stats.py. Also include a function
named mean, which computes the average of a set of numbers. Each function should
expect a list of numbers as an argument and return a single number. Each
function should return 0 if the list is empty. Include a main function that
tests the three statistical functions with a given list.

An example of the program output is shown below:

List: [3, 1, 7, 1, 4, 10]
Mode: 1
Median: 3.5
Mean: 4.33333333333333
"""

def main():
"""
    nums = [9, 2, 4, 3]

    print("mean test ", end='')
    stats_test(mean(nums), 4.5)

    print("median test for even number of elements ", end='')
    stats_test(median(nums), 3.5)

    print("median test for odd number of elements ", end='')
    nums.append(4)
    stats_test(median(nums), 4)

    print("mode test ", end='')
    nums.extend([3, 3])
    stats_test(mode(nums), 3)
"""
    nums = input("List: ")
    print("Mode: ", mode(nums))
    print("Median: ", median(nums))
    print("Mean: ", mean(nums))

def stats_test(actual, expected):
    if actual == expected:
        print("passes")
    else:
        print("fails")


def mean(numbers):
    total = 0.0
    for num in numbers:
        total += num
    return total / len(numbers)


def median(numbers):
    size = len(numbers)
    numbers = sorted(numbers)
    # if an odd number of numbers, pick the middle one
    mid = size // 2
    if size % 2 == 1:
        return numbers[mid]
    else:  # return the average of the middle two numbers
        return mean([numbers[mid], numbers[mid - 1]])


def mode(numbers):
    dyct = {}
    # count the elements
    for num in numbers:
        if dyct.get(num, None) is None:
            dyct[num] = 1
        else:
            dyct[num] += 1
    # find and return the most frequent
    largest = max(dyct.values())
    for key in dyct:
        if dyct[key] == largest:
            return key


if __name__ == "__main__":
    main()