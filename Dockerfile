FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /challenge

# Install Python dependencies
RUN pip install --no-cache-dir qrcode[pil] pillow

# Copy challenge files
COPY qr_challenge.py /challenge/
COPY setup-challenge.py /challenge/

# Create artifacts directory
RUN mkdir -p /challenge/cmgr/artifacts

# Set permissions
RUN chmod +x /challenge/setup-challenge.py

# Default command (setup will be run by the platform with FLAG env var)
CMD ["python3", "setup-challenge.py"]

