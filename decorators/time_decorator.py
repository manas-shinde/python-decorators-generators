import time
import logging
import functools

logger = logging.getLogger("decorators.time")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("[%(asctime)s] %(message)s"))
logger.addHandler(handler)


def time_execution(func):
    """Logs the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        logger.info(f"{func.__name__} took {end - start:.4f}s to execute.")
        return result
    return wrapper
