import logging
import time
import functools


# Configure logger at module level
logger = logging.getLogger("decorators.logging")
handler = logging.StreamHandler()
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s - %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def log_execution(func):
    """Decorator to log function execution with arguments and execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"Called `{func.__name__}` with args={args}, kwargs={kwargs}")
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            logger.info(f"`{func.__name__}` returned {result!r}")
            return result
        except Exception as e:
            logger.exception(f"Error in `{func.__name__}`: {e}")
            raise
        finally:
            end_time = time.time()
            logger.info(
                f"`{func.__name__}` took {end_time - start_time:.4f}s to execute")
    return wrapper
