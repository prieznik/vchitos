# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install system dependencies for Pygame
# These are required for the library to compile/run in a headless Linux environment
RUN apt-get update && apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libfreetype6-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project structure into the container
COPY . .

# Set environment variables for non-interactive execution
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Ensure the Python path includes the 'src' directory so imports work correctly
ENV PYTHONPATH="/app/src"

# Execute the main script located inside the src folder
CMD ["python", "src/main.py"]