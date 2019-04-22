"""
File: countfib.py
Prints the the number of calls of an iterative Fibonacci
function with problem sizes that double.
"""

from counter import Counter

def fib(n, counter = None):
    """Count the number of iterations in the Fibonacci
    function."""
    sum = 1
    first = 1
    second = 1
    count = 3
    while count <= n:
        if counter: counter.increment()
        sum = first + second
        first = second
        second = sum
        count += 1
    return sum

problemSize = 2
print("%12s%15s" % ("Problem Size", "Iterations"))
for count in range(5):
    counter = Counter()

    # The start of the algorithm
    fib(problemSize, counter)
    # The end of the algorithm
    
    print("%12d%15s" % (problemSize, counter))
    problemSize *= 2
