import time


# generator version of fib. this is the most efficient in python.
def generator_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# memoized_fib generates the fibonacci sequence using a memoization technique
def memoized_recursive_fib(n):
    memo = [None] * (n + 1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] is None:
        memo[n] = memoized_recursive_fib(n - 1) + memoized_recursive_fib(n - 2)
    return memo[n]


# recursive_fib generates the fibonacci sequence using a recursive algorithm
def naiive_recursive_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return naiive_recursive_fib(n - 1) + naiive_recursive_fib(n - 2)


# generating the sequences and timing the functions
if __name__ == '__main__':
    print('generator_fib:')
    start1 = time.time()
    count = 0
    for i in generator_fib():
        print(i)
        count = count + 1
        if count > 1000:
            break
    end1 = time.time()
    print('Time:', end1 - start1)
    print()

    print('memoized_recursive_fib:')
    start2 = time.time()
    for i in range(0, 20):
        print(memoized_recursive_fib(i))
    end2 = time.time()
    print('Time:', end2 - start2)
    print()

    print('naiive_recursive_fib:')
    start3 = time.time()
    for i in range(0, 20):
        print(naiive_recursive_fib(i))
    end3 = time.time()
    print()

    print('Time for generator_fib:', end1 - start1)
    print('Time for memoized_recursive_fib:', end2 - start2)
    print('Time for naiive_recursive_fib:', end3 - start3)
