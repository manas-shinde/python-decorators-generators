from decorators.time_decorator import time_execution


@time_execution
def add(x, y):
    return x + y


def test_time_execution():
    assert add(2, 5) == 7
