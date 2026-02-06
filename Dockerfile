# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Install system dependencies
# git is required for uv and version control interactions
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    make \
    && rm -rf /var/lib/apt/lists/*

# Install uv for fast package management
RUN pip install uv

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies using uv
RUN uv sync

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run tests by default
CMD ["make", "test"]
