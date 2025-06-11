import time
import functools
import logging

logger = logging.getLogger("decorators.benchmark")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("[%(asctime)s] %(message)s"))
logger.addHandler(handler)


def benchmark(threshold: float = 0.0):
    """Logs execution time. Warns if over threshold."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            if elapsed > threshold:
                logger.warning(
                    f"{func.__name__} took {elapsed:.4f}s (over threshold: {threshold}s)")
            else:
                logger.info(f"{func.__name__} executed in {elapsed:.4f}s")
            return result
        return wrapper
    return decorator
