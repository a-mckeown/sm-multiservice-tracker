# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install Flask

# Make port 5000 available to the world outside the container
EXPOSE 5001

# Run the application
CMD ["python", "order_service.py"]
