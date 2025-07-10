FROM php:8.2-cli

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        curl \
        unzip \
        libzip-dev \
    && rm -rf /var/lib/apt/lists/*

# Install PHP extensions
RUN docker-php-ext-install zip

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Copy composer files if they exist
COPY composer.json ./
COPY composer.lock* ./

# Install PHP dependencies (skip if composer.lock doesn't exist)
RUN if [ -f composer.lock ]; then composer install --optimize-autoloader --no-interaction; else composer install --optimize-autoloader --no-interaction; fi

# Copy the entire app directory
COPY app/ ./app/

# Add Composer vendor bin to PATH
ENV PATH="/app/vendor/bin:$PATH"

# Create a non-root user
RUN useradd --create-home --shell /bin/bash developer \
    && chown -R developer:developer /app
USER developer

# Default command
CMD ["php", "-S", "0.0.0.0:8000", "-t", "app/src"] 