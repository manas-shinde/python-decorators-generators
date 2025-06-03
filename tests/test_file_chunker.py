import tempfile
from generators.file_chunker import file_chunker


def test_file_chunker_reads_data():
    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as tf:
        tf.write(b"abcdefghij" * 100)

    chunks = list(file_chunker(tf.name, chunk_size=100))
    assert sum(len(c) for c in chunks) == 1000
