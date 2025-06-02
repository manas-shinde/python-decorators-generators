from decorators.retry_decorator import retry_on_exception


@retry_on_exception(retries=3, delay=2, exceptions=(ZeroDivisionError,))
def unstable_division(x, y):
    return x / y


if __name__ == "__main__":
    unstable_division(10, 0)
