def file_chunker(file_path: str, chunk_size: int = 1024):
    with open(file_path, "r") as f:
        while chunk := f.read(chunk_size):
            yield chunk
