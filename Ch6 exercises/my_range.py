def myRange(start, stop=None, step=None):
    if stop == None:
        if start <= 0:
            return []
        else:
            step = 1
            stop = start
            start = 0
    elif step == None:
        if start >= stop:
            return []
        else:
            step = 1
    elif step == 0:
        print("Invalid step argument:")

    # print(start, stop, step)
    if start >= stop and step > 0 \
            or start <= stop and step < 0:
        return []
    else:
        return [start] + myRange(start + step, stop, step)


def main():
    print(myRange(0))
    print(myRange(3))
    print(myRange(-1))
    print(myRange(0, 1))
    print(myRange(2, 5))
    print(myRange(0, -3))
    print(myRange(0, -3, -1))
    print(myRange(5, 1, -1))
    print(myRange(10))
    print(myRange(1, 10, 2))
    print(myRange(10, 1, -1))
    print(myRange(4, 12, 2))

if __name__ == '__main__':
    main()
