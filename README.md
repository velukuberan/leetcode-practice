# Leetcode Practice
My personal Leet Code practice solutions, implemented in Python, PHP and Typescript, with a focus on data structures and algorithms.

[![codecov](https://codecov.io/github/velukuberan/leetcode-practice/graph/badge.svg?token=J22M5AH8QJ)](https://codecov.io/github/velukuberan/leetcode-practice)

## 🐳 Docker Setup

This project uses Docker for a seamless development environment across all three languages.

### Quick Start

1. **Build and start all services:**
   ```bash
   make build
   make up
   ```

2. **Run tests for all languages:**
   ```bash
   make test
   ```

3. **Access individual language environments:**
   ```bash
   make shell-python    # Python container
   make shell-php       # PHP container
   make shell-typescript # TypeScript container
   ```

### Available Commands

- `make help` - Show all available commands
- `make build` - Build all Docker containers
- `make up` - Start all services
- `make down` - Stop all services
- `make logs` - Show logs from all services
- `make clean` - Remove containers, networks, and volumes
- `make test` - Run tests for all languages
- `make python-test` - Run Python tests only
- `make php-test` - Run PHP tests only
- `make typescript-test` - Run TypeScript tests only

### Manual Docker Commands

If you prefer using docker-compose directly:

```bash
# Build containers
docker-compose build

# Start services
docker-compose up -d

# Run Python tests
docker-compose run --rm python python -m pytest

# Run PHP tests
docker-compose run --rm php composer test

# Run TypeScript tests
docker-compose run --rm typescript npm test

# Access shell in any container
docker-compose exec python bash
docker-compose exec php bash
docker-compose exec typescript sh
```

### Project Structure

```
leetcode-practice/
├── docker-compose.yml          # Root orchestration
├── Makefile                    # Convenient commands
├── .dockerignore              # Docker ignore rules
├── python/
│   ├── Dockerfile             # Python container
│   ├── pyproject.toml         # Python dependencies
│   └── src/                   # Python solutions
├── php/
│   ├── Dockerfile             # PHP container
│   ├── composer.json          # PHP dependencies
│   └── src/                   # PHP solutions
└── typescript/
    ├── Dockerfile             # TypeScript container
    ├── package.json           # TypeScript dependencies
    ├── tsconfig.json          # TypeScript config
    └── src/                   # TypeScript solutions
```

### Development Workflow

1. **Start the environment:** `make up`
2. **Write your solution** in the appropriate language folder
3. **Run tests:** `make test` or language-specific test command
4. **Access container shell** for debugging: `make shell-python`
5. **Stop environment:** `make down`

Each language container has its own isolated environment with all necessary tools and dependencies pre-installed.