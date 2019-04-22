def printAll(seq):
    if seq:
        print("arg =", seq)
        print(seq[0])
        printAll(seq[1:])


def main():
    # test lists
    print("Iteratve sequences")
    printAll([])
    printAll([1])
    printAll(['a', 'c', 'y', 'z'])

    # test string
    print("String sequences")
    printAll('')
    printAll('1')
    printAll('now is')

    # test tuples
    print("Tuple sequences")
    printAll(())
    printAll((a, z))
    printAll((1, 2), (3, 4))


if __name__ == '__main__':
    main()
