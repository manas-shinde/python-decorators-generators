from generators.paginated_api_reader import paginated_api_reader


def mock_api(page):
    if page > 3:
        return [], False
    return [f"item-{page}-{i}" for i in range(2)], True


def test_paginated_api_reader():
    items = list(paginated_api_reader(mock_api))
    assert len(items) == 6
    assert items[0] == "item-1-0"
    assert items[-1] == "item-3-1"
