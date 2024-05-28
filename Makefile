APP_NAME = app.main:app
HOST = 127.0.0.1
PORT = 8080

POETRY_RUN = poetry run

.PHONY: help
help:
	@echo "Makefile commands:"
	@echo "  make install      - Install project dependencies"
	@echo "  make run          - Run the FastAPI application"
	@echo "  make lint         - Lint the code using flake8"
	@echo "  make format       - Format the code using black"
	@echo "  make test         - Run tests using pytest"
	@echo "  make clean        - Clean up temporary files"

.PHONY: install
install:
	poetry install

.PHONY: run
run:
	$(POETRY_RUN) uvicorn $(APP_NAME) --host $(HOST) --port $(PORT) --reload

.PHONY: lint
lint:
	$(POETRY_RUN) flake8 .

.PHONY: format
format:
	$(POETRY_RUN) black .

.PHONY: test
test:
	$(POETRY_RUN) pytest

.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -exec rm -f {} +
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
