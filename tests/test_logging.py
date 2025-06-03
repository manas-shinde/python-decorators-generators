from decorators.logging_decorator import log_execution


@log_execution
def add(a, b):
    return a + b


def test_log_execution():
    assert add(2, 3) == 5
    print("Success")
