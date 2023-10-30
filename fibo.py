# Fibonacci numbers module
# https://docs.python.org/3/tutorial/modules.html
# https://en.wikipedia.org/wiki/Fibonacci_sequence


def fib(n):
    """
        An algorithm for displaying Fibonacci sequence.
        Write Fibonacci series up to n
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    """
        An algorithm for returning a Fibonacci sequence.
        Return Fibonacci series up to n
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
