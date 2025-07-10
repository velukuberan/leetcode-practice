FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install --no-cache-dir uv

# Copy pyproject.toml first for better caching
COPY pyproject.toml .

# Install Python dependencies using uv (system-wide)
RUN uv pip install --system -e . \
    && uv pip install --system mypy pytest pytest-cov ruff

# Copy the entire app directory
COPY app/ ./app/

# Create a non-root user
RUN useradd --create-home --shell /bin/bash developer \
    && chown -R developer:developer /app
USER developer

# Default command (can be overridden in docker-compose)
CMD ["python", "-m", "pytest"] 