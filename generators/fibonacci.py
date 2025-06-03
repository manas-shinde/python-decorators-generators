def fibonacci():
    """Generates the infinite Fibonacci sequence."""
    a, b = 0, 1

    while True:
        yield a
        a, b = b, (a+b)
