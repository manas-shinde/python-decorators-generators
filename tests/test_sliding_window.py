from generators.sliding_window import sliding_window


def test_sliding_window():
    result = list(sliding_window(range(5), 3))
    assert result == [(0, 1, 2), (1, 2, 3), (2, 3, 4)]
