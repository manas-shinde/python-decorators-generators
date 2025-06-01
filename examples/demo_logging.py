from decorators.logging_decorator import log_execution


@log_execution
def add(a, b):
    return a + b


@log_execution
def divide(x, y):
    return x / y


if __name__ == "__main__":
    add(10, 20)
    try:
        divide(10, 0)
    except ZeroDivisionError:
        pass
