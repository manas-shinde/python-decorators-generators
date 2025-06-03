import time


def tail_reader(filepath, interval=1.0):
    """Generator that yields new lines from a file as they're written."""
    with open(filepath, 'r') as f:
        f.seek(0, 2)  # Move to EOF
        while True:
            line = f.readline()
            if not line:
                time.sleep(interval)
                continue
            yield line.strip()
