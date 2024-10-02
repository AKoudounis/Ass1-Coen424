# Use the official lightweight Python image
FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# Set the working directory
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy the requirements file and install production dependencies first
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and generated files
COPY ./generated /app/generated
COPY ./proto /app/proto  
COPY ./server.py /app/  


# Expose the gRPC port
EXPOSE 50051

# Command to run the gRPC application
CMD ["python", "server.py"]