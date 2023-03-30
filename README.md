# DD2482-CD-Demo
Demo project for KTH DevOps course demonstrating continuous delivery with GitHub actions

# Docker Python Test Server

This is a simple guide on how to use Docker to build and run a Python test server.

## Prerequisites
Make sure you have Docker installed on your machine. If not, you can download and install it from the official website: https://www.docker.com/

## Building the Docker Image
To build the Docker image, run the following command in your terminal:

```
docker build -t python-test-server .
````
This command will build the image and tag it as python-test-server.

## Running the Docker Container
To run the Docker container, use the following command:

```
docker run -it -p 80:5000 --rm --name python-server-test python-test-server
````

This command will start the container and map port 80 on your local machine to port 5000 inside the container. It will also automatically remove the container when it's stopped, and name the container as python-server-test.

That's it! You now have a Docker container running a Python test server. You can access the server by going to http://localhost in your web browser.

