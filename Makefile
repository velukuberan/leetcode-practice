.PHONY: help build up down logs clean python test python-test php-test typescript-test shell-python shell-php shell-typescript

# Default target
help:
	@echo "Available commands:"
	@echo "  build        - Build all Docker containers"
	@echo "  up           - Start all services"
	@echo "  down         - Stop all services"
	@echo "  logs         - Show logs from all services"
	@echo "  clean        - Remove containers, networks, and volumes"
	@echo "  python       - Run Python"
	@echo "  test         - Run tests for all languages"
	@echo "  python-test  - Run Python tests"
	@echo "  php-test     - Run PHP tests"
	@echo "  typescript-test - Run TypeScript tests"
	@echo "  shell-python - Open shell in Python container"
	@echo "  shell-php    - Open shell in PHP container"
	@echo "  shell-typescript - Open shell in TypeScript container"

# Build all containers
build:
	docker-compose build

# Start all services
up:
	docker-compose up -d

# Stop all services
down:
	docker-compose down

# Show logs
logs:
	docker-compose logs -f

# Clean everything
clean:
	docker-compose down -v --rmi all

# Run Python file - Fixed to handle arguments properly
python:
	@if [ "$(filter-out $@,$(MAKECMDGOALS))" = "" ]; then \
		docker-compose run --rm python python; \
	else \
		docker-compose run --rm python python $(filter-out $@,$(MAKECMDGOALS)); \
	fi

# This prevents Make from treating arguments as targets
%:
	@:

# Run all tests
test: python-test php-test typescript-test

# Python tests
python-test:
	docker-compose run --rm python python -m pytest

# PHP tests
php-test:
	docker-compose run --rm php composer test

# TypeScript tests
typescript-test:
	docker-compose run --rm typescript npm test

# Shell access
shell-python:
	docker-compose exec python bash

shell-php:
	docker-compose exec php bash

shell-typescript:
	docker-compose exec typescript sh 
