# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    postgresql \
    && rm -rf /var/lib/apt/lists/*

# Install project dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Make port 8000 available outside this container
EXPOSE 8000

# Run the application
CMD ["gunicorn", "bookstore.wsgi:application", "--bind", "0.0.0.0:8000"]
