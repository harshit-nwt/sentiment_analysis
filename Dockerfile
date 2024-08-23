# # Use an official Python runtime as a parent image
# FROM python:3.11-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Define environment variable
# ENV DJANGO_SETTINGS_MODULE=sentiment_nwt_project.settings

# # Run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Define an alias for the specific python version used in this file.
FROM python:3.11.2-bullseye
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file into the container at /app
COPY requirements.txt .
# Upgrade pip and install required dependencies
RUN pip install --upgrade pip setuptools wheel
RUN apt-get update && apt-get install -y build-essential libffi-dev libbz2-dev zlib1g-dev
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of your application code into the container
COPY . .
# Make port 8000 available to the world outside this container
EXPOSE 8000
# Define environment variable
ENV DJANGO_SETTINGS_MODULE=sentiment_nwt_project.settings