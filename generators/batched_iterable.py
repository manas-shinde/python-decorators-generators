def batched_iterable(iterable, batch_size: int):
    """Yields items from iterable in batches of `batch_size`."""
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch
