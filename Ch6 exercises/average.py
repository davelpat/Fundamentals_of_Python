import os
import os.path
from functools import reduce

def read_nums_from(filename):
    if not os.path.isfile(filename):
        print("No such file:", filename)
        return False
    else:
        f = open(filename, 'r')
        str_nums = f.read().split()
        return list(map(int, str_nums))

def average(numbers):
    return reduce(lambda x, y: x+y, numbers) / len(numbers)

def main():
    filename = input("Enter the input file name: ")
    numbers = read_nums_from(filename)
    print("The average is", average(numbers))

if __name__ == '__main__':
    main()