import csv


def csv_row_reader(filepath):
    """Yields rows from a CSV file as dictionaries (using header row)."""
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row
