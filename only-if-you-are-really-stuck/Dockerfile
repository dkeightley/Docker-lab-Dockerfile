# Our base image
FROM python:alpine

# Lets work out of /usr/src/app in the container
WORKDIR /usr/src/app

# Copy files required for the app to run
COPY . .

# Install Python modules needed by the Python app
RUN pip install --no-cache-dir -r requirements.txt

# The port number the container should expose
EXPOSE 5000

# Run the application
CMD ["python", "./app.py"]
