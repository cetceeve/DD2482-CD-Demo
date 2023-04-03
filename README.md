# DD2482-CD-Demo
Demo project for KTH DevOps course demonstrating continuous delivery with GitHub actions

## Docker Python Test Server

This is a simple guide on how to use Docker to build and run a Python test server.

### Prerequisites
Make sure you have Docker installed on your machine. If not, you can download and install it from the official website: https://www.docker.com/

### Building the Docker Image
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

## Resources to Setup the AWS Cluster

A good starting point is Githubs Guide on how to deploy to AWS ECS.
https://docs.github.com/en/actions/deployment/deploying-to-your-cloud-provider/deploying-to-amazon-elastic-container-service

When working with AWS it is easy to pay for something unexpectedly.
This resource can help you avoid paying by accident.
https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all

Your most important resource is the AWS ECS documentation.
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/get-set-up-for-amazon-ecs.html

Make sure you understand the difference between AWS EC2 and AWS Fargate and their respective
pricing models. https://containersonaws.com/introduction/ec2-or-aws-fargate/

Documentation of ECS task definition parameters.
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html

Load Balancers allow us to have a consistent web-address even if the underlying
infrastructure is replaced by AWS.
https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html

Nice video showcasing the core parts of an ECS Deployment.
https://youtu.be/PgyFrkJaNys