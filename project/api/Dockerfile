# syntax=docker/dockerfile:1
FROM python:3.12-slim AS runtime
ARG APP_HOME=/app

FROM python:3.12 AS builder
ARG APP_HOME=/app
WORKDIR ${APP_HOME}
COPY pyproject.toml poetry.lock*? .
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction
COPY . .
RUN poetry build

FROM runtime
ARG APP_HOME=/app
WORKDIR ${APP_HOME}
RUN pip install --no-cache-dir gunicorn uvicorn[standard]
COPY --from=builder ${APP_HOME}/dist/*.whl .
RUN pip install --no-cache-dir ./*.whl && rm -f ./*.whl
ENV PORT=8000
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s CMD python -c "import os, sys, urllib.request; urllib.request.urlopen(f'http://127.0.0.1:{os.getenv(\"PORT\", \"8000\")}/health')"
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "todo_app.main:app", "--bind", "0.0.0.0:8000"]
