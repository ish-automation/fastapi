"""Simple benchmark script for FastAPI."""

import time
from fastapi.testclient import TestClient
from docs_src.example_project.main import app

client = TestClient(app)

if __name__ == "__main__":
    start = time.perf_counter()
    for _ in range(100):
        response = client.get("/")
        assert response.status_code == 200
    duration = time.perf_counter() - start
    print(f"100 requests took {duration:.4f} seconds")
