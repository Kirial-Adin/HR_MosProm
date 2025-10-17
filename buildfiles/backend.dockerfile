FROM python:3.12-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    UV_NO_SYNC=1

WORKDIR /app

FROM base AS uv-installer
COPY --from=ghcr.io/astral-sh/uv:0.7.20 /uv /bin/uv

FROM uv-installer AS deps
WORKDIR /app
COPY ../back-end/pyproject.toml uv.lock* ./
RUN uv venv && uv sync --no-dev

FROM uv-installer AS app
WORKDIR /app
COPY --from=deps /app/.venv ./.venv
COPY ../back-end .
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
