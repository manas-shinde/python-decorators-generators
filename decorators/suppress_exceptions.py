import functools
import logging

logger = logging.getLogger("decorators.suppress")


def suppress_exceptions(default=None, exceptions=(Exception,), log=True):
    """Suppress specified exceptions and optionally log them."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                if log:
                    logger.warning(
                        f"Suppressed exception in {func.__name__}: {e}")
                return default
        return wrapper
    return decorator
