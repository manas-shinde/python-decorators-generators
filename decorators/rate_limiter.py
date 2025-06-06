import time
import threading
import functools


def rate_limiter(calls_per_second):
    interval = 1 / calls_per_second
    lock = threading.Lock()
    last_called = [0.0]

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                now = time.time()
                wait = interval - (now - last_called[0])
                if wait > 0:
                    time.sleep(wait)
                last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator
