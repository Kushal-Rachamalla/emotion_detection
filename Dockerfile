# Use a base image with Python + pip
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose the port Flask uses
EXPOSE 8000

# Start the server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
