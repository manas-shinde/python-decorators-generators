from decorators.memoize import memoize


@memoize
def square(x):
    return x * x


def test_memoize():
    assert square(3) == 9
    assert square(3) == 9  # returned from cache
    assert square(4) == 16
