# Performance Benchmarks

You can run a simple benchmark locally with:

```bash
python benchmarks/simple_benchmark.py
```

This uses FastAPI's `TestClient` to make 100 requests to the example application
and prints the total time taken.
