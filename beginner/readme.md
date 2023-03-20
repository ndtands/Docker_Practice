## Docker Concepts:
- Docker images: Docker image is a lightweight, standalon, and executable package that contains all the nescessary software to run application .
- Docker containers: Docker container is a runing instance of a Docker Image
- Docker registries: Docker registry is a place where Docker images are stored and distributed
- Docker networks: A Docker network is a virtual network that connects Docker containers
- Docker volumes: Docker volume is a persistent data storage solution for DOcker containers

## Some command:
```
    # start new Docker container
    docker run

    # List all docker cotainer running
    docker ps

    # Stop container
    docker stop <container-id>

    # Remove container
    docker rm <container-id>

    # logs
    docker logs <container-id>
```

## Create first image 
Now that you have a basic understanding of Docker, it's time to create your first Docker image. The following steps will help you create an image:
- Write a Dockerfile
- Build the Docker image
- Run the Docker container