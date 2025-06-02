import functools
import time
import logging

logger = logging.getLogger("decorators.retry")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(message)s"))
logger.addHandler(handler)


def retry_on_exception(retries=3, delay=1, exceptions=(Exception,)):
    """Retry the decorated function if it raises one of the specified exceptions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f"Attempt {attempt} failed: {e}")
                    if attempt == retries:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator
