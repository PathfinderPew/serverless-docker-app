# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install required packages, curl, and Node.js v18
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g serverless

# Copy the current directory contents into the container at /app
COPY . /app

# Install any Python dependencies
RUN pip install -r requirements.txt