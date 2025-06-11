import functools


def once(func):
    """Ensure a function runs only once. Returns cached result thereafter."""
    result_cache = {}
    has_run = False

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal has_run
        if not has_run:
            result_cache['result'] = func(*args, **kwargs)
            has_run = True
        return result_cache['result']
    return wrapper
