import tempfile
import csv
from generators.csv_row_reader import csv_row_reader


def test_csv_row_reader():
    with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name"])
        writer.writeheader()
        writer.writerow({"id": "1", "name": "Alice"})
        writer.writerow({"id": "2", "name": "Bob"})
        path = f.name

    rows = list(csv_row_reader(path))
    assert len(rows) == 2
    assert rows[0]["name"] == "Alice"
