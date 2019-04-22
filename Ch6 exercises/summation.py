def summation (lower, upper, step=1, func=lambda x: x):
    total = 0
    for num in range(lower, upper+1, step):
        total += func(num)
    return total
