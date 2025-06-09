from generators.batched_iterable import batched_iterable


def test_batches():
    data = list(range(10))
    batches = list(batched_iterable(data, 4))
    assert batches == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]
