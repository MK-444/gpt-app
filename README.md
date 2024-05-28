# Setup and Run

---
## Run with Docker

---

1. ```bash
   docker build -t granton-test-assignment .
   ```

2. ```bash
   docker run -p 8001:8000 granton-test-assignment
   ```

## Run with Make

---

**Install project dependencies**

```bash
make install
```

**Run the FastAPI application**

```bash
make run
```

**Run tests using pytest**

```bash
make test
```