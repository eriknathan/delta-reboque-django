FROM python:3.9.16-slim-buster
LABEL authors="eriknathan"

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8000 for the Django development server
EXPOSE 8000

# Define environment variable for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Start the Django development server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]