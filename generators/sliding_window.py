from collections import deque


def sliding_window(iterable, size):
    """Yields sliding windows of the given size from an iterable."""
    it = iter(iterable)
    window = deque(maxlen=size)

    for item in it:
        window.append(item)
        if len(window) == size:
            yield tuple(window)
