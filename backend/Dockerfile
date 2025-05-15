# # Use official Python image
# FROM python:3.10-slim

# # Create app directory inside container
# WORKDIR /app

# # Install system dependencies for mysqlclient
# RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev && rm -rf /var/lib/apt/lists/*

# # Copy backend code
# COPY . /app

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Set environment
# ENV PYTHONUNBUFFERED=1

# # Expose port
# EXPOSE 8000

# # Start the FastAPI app
# CMD ["uvicorn", "api_creation:app", "--host", "0.0.0.0", "--port", "8000"]


# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose the port your FastAPI app runs on
EXPOSE 8000

# Run the app
CMD ["uvicorn", "api_creation:app", "--host", "0.0.0.0", "--port", "8000"]
