import time
import functools


def deprecated(func):
    @functools.wraps(func)
    def wrapper():
        print("Warning!!!")
    return wrapper
