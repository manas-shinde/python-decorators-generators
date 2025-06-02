from decorators.time_decorator import time_execution


@time_execution
def loop():
    for i in range(100000000):
        pass


if __name__ == "__main__":
    loop()
