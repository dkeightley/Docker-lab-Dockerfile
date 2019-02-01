# Our base image
FROM python:alpine

# Lets work out of /usr/src/app in the container
WORKDIR /usr/src/app

# Copy requirements.txt first
COPY requirements.txt .

# Install Python modules needed by the Python app
RUN pip install --no-cache-dir -r requirements.txt

# The port number the container should expose
EXPOSE 5000

# Run the application
CMD ["python", "./app.py"]

# Copy remaining files required for the app to run
COPY . .
