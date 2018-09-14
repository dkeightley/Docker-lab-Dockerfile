# Dockerfile Lab

Our manager has tasked us with a very important project, aparently customers are complaining that our Random Cat Generator has been down for some time. It's super urgent - Sev 1, interwebs down/down or something.

We only know a little bit about the app, and that the previous engineer who deployed it was our Senior Principal Full Stack Engineer who rage quit, and now all we have is the source code.

So far we know:

- It's a Python app
- Theres some requirements and that it ran in Docker before
- We can configure the container to listen on any port we like
- It was based on the ```python:alpine``` docker image

### Steps

- Clone this repository
- Create a Dockerfile for this Python app
- Build a container image with the Dockerfile
- Run a container from the image and load the app in a browser
