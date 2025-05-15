# Use official Python image
FROM python:3.10-slim

# Create app directory inside container
WORKDIR /app

# Install system dependencies for mysqlclient
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev && rm -rf /var/lib/apt/lists/*

# Copy backend code
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "api_creation:app", "--host", "0.0.0.0", "--port", "8000"]
