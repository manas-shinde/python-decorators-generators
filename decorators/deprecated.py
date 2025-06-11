import warnings
import functools


def deprecated(reason="This function is deprecated"):
    """Emit a warning when the function is called."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(f"{func.__name__} is deprecated: {reason}",
                          DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator
