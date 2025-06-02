import functools
import time

_cache = {}


def cache_result(ttl_seconds=60):
    """Caches the function result in memory for the given TTL."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(_cache)
            key = (func.__name__, args, frozenset(kwargs.items()))
            now = time.time()

            if key in _cache:
                result, timestamp = _cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            result = func(*args, **kwargs)
            _cache[key] = (result, now)
            return result
        return wrapper
    return decorator
