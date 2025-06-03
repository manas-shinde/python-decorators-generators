import time
from decorators.cache_decorator import cache_result


@cache_result(ttl_seconds=2)
def slow_square(x):
    time.sleep(1)
    return x * x


def test_cache_result():
    start = time.time()
    assert slow_square(3) == 9
    first_duration = time.time() - start

    start = time.time()
    assert slow_square(3) == 9  # From cache
    second_duration = time.time() - start

    assert second_duration < first_duration  # Cached
