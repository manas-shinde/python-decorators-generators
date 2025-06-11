import os
import time


def directory_watcher(path, interval=1.0):
    """
    Yields new filenames in a directory as they appear.
    """
    seen = set(os.listdir(path))

    while True:
        time.sleep(interval)
        current = set(os.listdir(path))
        new_files = current - seen
        for file in new_files:
            yield file
        seen = current
