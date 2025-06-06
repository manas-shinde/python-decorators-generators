import functools
import inspect


def validate_types(func):
    """Decorator to enforce type hints at runtime."""
    sig = inspect.signature(func)
    print(sig)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        for name, value in bound.arguments.items():
            expected = sig.parameters[name].annotation
            if expected is not inspect._empty and not isinstance(value, expected):
                raise TypeError(
                    f"Argument '{name}' must be {expected}, got {type(value)}")

        result = func(*args, **kwargs)
        if sig.return_annotation is not inspect._empty and not isinstance(result, sig.return_annotation):
            raise TypeError(
                f"Return value must be {sig.return_annotation}, got {type(result)}")
        return result

    return wrapper
