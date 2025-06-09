def paginated_api_reader(fetch_page_func, start=1):
    """
    Yields items from a paginated API.

    `fetch_page_func(page_number)`: should return (items: list, has_more: bool)
    """
    page = start
    while True:
        items, has_more = fetch_page_func(page)
        for item in items:
            yield item
        if not has_more:
            break
        page += 1
