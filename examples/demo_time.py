from decorators.time_decorator import time_execution


@time_execution
def long_for_loop():
    for i in range(100000000):
        pass


if __name__ == "__main__":
    long_for_loop()
