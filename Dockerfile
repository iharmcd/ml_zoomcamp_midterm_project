# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port your app runs on
EXPOSE 9696

# Command to run the application
CMD ["python", "app.py"]
