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
COPY ./proto /app/proto  # Add this if you need to generate the protobuf files
COPY ./server.py /app/  # Don't forget to copy your server code

# Optionally generate protobuf files (if needed)
# RUN python -m grpc_tools.protoc -I./proto --python_out=./generated --grpc_python_out=./generated ./proto/*.proto

# Expose the gRPC port
EXPOSE 50051

# Command to run the gRPC application
CMD ["python", "server.py"]