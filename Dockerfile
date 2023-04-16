# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application source code into the container
COPY . .

# Expose the port on which the Flask application will run
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
