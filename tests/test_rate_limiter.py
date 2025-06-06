import time
from decorators.rate_limiter import rate_limiter

calls = []


# Max 2 calls per second = 0.5s delay between calls
@rate_limiter(calls_per_second=2)
def limited_func(x):
    calls.append(time.time())
    return x * 2


def test_rate_limiter_timing():
    calls.clear()
    for i in range(3):
        limited_func(i)

    assert len(calls) == 3
    assert (calls[1] - calls[0]) >= 0.49
    assert (calls[2] - calls[1]) >= 0.49
