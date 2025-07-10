FROM node:18-alpine

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    git \
    curl

# Copy package files
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm ci --only=production

# Copy TypeScript config
COPY tsconfig.json ./

# Create src directory and copy source code
RUN mkdir -p src
COPY src/ ./src/

# Create a non-root user
RUN addgroup -g 1001 -S nodejs \
    && adduser -S nodejs -u 1001
USER nodejs

# Default command
CMD ["npm", "start"] 