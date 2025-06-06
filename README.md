# Python Decorators & Generators

A curated collection of production-ready, reusable Python decorators and generators — crafted using modern Python best practices.

This package includes:

- ✅ Common decorators like logging, retrying, caching, and timing
- ✅ Generators for streaming data, infinite sequences, and efficient file processing
- ✅ Unit tests and GitHub Actions CI
- ✅ Editable install via `pyproject.toml` for clean imports

---

## 📦 Installation (Editable Mode)

Make sure you have Python 3.8+ and `pip`:

```bash
git clone https://github.com/your-username/python-decorators-generators.git
```

```bash
cd python-decorators-generators
```

```bash
pip install -e .
```

✅ Decorators Included
Decorator Description
log_execution Logs function calls, arguments, return values, execution time, and exceptions
retry_on_exception Retries a function on failure, with configurable retry count and delay
cache_result In-memory caching with TTL support
time_execution Logs how long a function takes to run

## 📂 Project Structure

```bash
python-decorators-generators/
├── decorators/
│ ├── logging*decorator.py
│ ├── retry_decorator.py
│ ├── cache_decorator.py
│ └── time_decorator.py
│
├── generators/
│ ├── fibonacci.py
│ ├── file_chunker.py
│ └── tail_reader.py
│
├── examples/
│ └── demo*<name>.py
│
├── tests/
│ └── test\_<name>.py
│
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

### ✅ Decorators Included

| Decorator            | Module                         | Description                                                               |
| -------------------- | ------------------------------ | ------------------------------------------------------------------------- |
| `log_execution`      | `decorators.logging_decorator` | Logs function calls, arguments, return values, execution time, and errors |
| `retry_on_exception` | `decorators.retry_decorator`   | Retries a function on failure, with customizable retry count and delay    |
| `cache_result`       | `decorators.cache_decorator`   | In-memory caching with configurable TTL                                   |
| `time_execution`     | `decorators.time_decorator`    | Logs how long a function takes to run                                     |

---

### 🔁 Generators Included

| Generator        | Module                    | Description                                                   |
| ---------------- | ------------------------- | ------------------------------------------------------------- |
| `fibonacci()`    | `generators.fibonacci`    | Infinite lazy sequence of Fibonacci numbers                   |
| `file_chunker()` | `generators.file_chunker` | Reads large files in fixed-size chunks using lazy loading     |
| `tail_reader()`  | `generators.tail_reader`  | Mimics `tail -f` to stream new lines from a file in real-time |

---

### 🧪 Run Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
pytest tests/
```

---

## 🚀 CI/CD with GitHub Actions

This project includes a CI pipeline that runs on every push and PR to main, defined in .github/workflows/python-tests.yml.
🧠 Why This Repo?

This repository is ideal for:

- Engineers who want reusable decorator utilities

- Data engineers working with large files or streams

- Anyone who wants to understand Python’s advanced features through real code

---

## 📬 Contributions

Feel free to fork this project, add more utilities (e.g., memoization, rate-limiting), or improve tests and documentation.

---

Let me know if you'd like a corresponding `pyproject.toml` now, or a downloadable `.zip` with the full folder setup.
