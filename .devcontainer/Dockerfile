FROM python:bookworm

# Set working directory
WORKDIR /workspace

# Install required system libraries (e.g., for matplotlib)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir pandas matplotlib

# Create output directory (optional if you mount it)
RUN mkdir -p /workspace/output
