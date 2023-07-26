# Use an official Python runtime as a base image
FROM python:3.4-alpine

# Set the working directory in the container to /code
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Flask app to listen on
EXPOSE 8000

# Command to run the Flask app when the container is launched
CMD ["python", "app.py"]

