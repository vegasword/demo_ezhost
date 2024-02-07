# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./script.py /app

# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# Run script.py when the container launches
CMD ["python3", "script.py"]
