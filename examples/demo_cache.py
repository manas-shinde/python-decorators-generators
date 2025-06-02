from decorators.cache_decorator import cache_result
import time


@cache_result(ttl_seconds=10)
def expensive_call(x):
    time.sleep(3)
    return x * x


print(expensive_call(5))  # takes 3s
print(expensive_call(5))  # fast
