# Dockerfile for DevSquad SvelteKit Application
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm ci

# Copy source and build
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine AS production

WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm ci --omit=dev

# Copy built application from builder
COPY --from=builder /app/build ./build

EXPOSE 3000

ENV NODE_ENV=production
ENV PORT=3000

CMD ["node", "build/index.js"]
