# Use the official lightweight Python image
FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED=True

# Set the working directory
WORKDIR /app

# Copy the requirements file and install production dependencies first
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application folder
COPY . .

# Expose the gRPC port
EXPOSE 443

# Command to run the gRPC application
CMD ["python", "server.py"]