# ---------- Build stage: install dependencies with Poetry ----------
FROM python:3.12-slim AS builder

ENV POETRY_VERSION=2.5.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PIP_NO_CACHE_DIR=1

RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --only main --no-root

# ---------- Runtime stage: just Python, the virtualenv and the app ----------
FROM python:3.12-slim

ENV PATH="/app/.venv/bin:${PATH}" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY app.py content.py ./
COPY templates ./templates
COPY static ./static

RUN useradd --create-home app_user
USER app_user

EXPOSE 8080

# Cloud Run sets $PORT; Gunicorn must listen on it on all interfaces.
CMD exec gunicorn --bind "0.0.0.0:${PORT}" --workers 1 --threads 8 --timeout 0 app:app
