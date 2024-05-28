FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

RUN apk update && \
    apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    postgresql-dev \
    gcc \
    musl-dev \
    curl \
    python3-dev \
    py3-pip

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

RUN poetry --version

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN cat /app/pyproject.toml && cat /app/poetry.lock

RUN poetry install --no-root --no-dev -vvv || { echo 'Poetry install failed' ; exit 1; }

COPY . /app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
