.PHONY: help test lint type-check format check coverage clean install dev

# Default target
help:
	@echo "Available commands:"
	@echo "  install     - Install dependencies"
	@echo "  dev         - Install development dependencies"
	@echo "  test        - Run tests"
	@echo "  coverage    - Run tests with coverage"
	@echo "  lint        - Run ruff linter"
	@echo "  format      - Format code with ruff"
	@echo "  type-check  - Run mypy type checker"
	@echo "  check       - Run all checks (lint, type-check, test)"
	@echo "  clean       - Clean up generated files"
	@echo "  versions    - Show tool versions"

# Install dependencies
install:
	uv sync

# Install development dependencies
dev:
	uv add --dev ruff mypy pytest pytest-cov

# Run tests
test:
	pytest -v

# Run tests with coverage
coverage:
	pytest --cov=. --cov-report=html --cov-report=term-missing

# Run linter
lint:
	ruff check .

# Format code
format:
	ruff format .

# Run type checker
type-check:
	mypy .

# Run all checks
check: lint type-check test

# Clean up generated files
clean:
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/

# Show tool versions
versions:
	@echo "Tool versions:"
	@python --version
	@pytest --version
	@ruff --version
	@mypy --version