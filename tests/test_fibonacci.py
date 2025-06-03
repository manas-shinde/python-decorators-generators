from generators.fibonacci import fibonacci

def test_fibonacci():
    fib = fibonacci()
    results = [next(fib) for _ in range(6)]
    assert results == [0, 1, 1, 2, 3, 5]
