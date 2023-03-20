## 1. Docker Compose
Docker Compose is a tool for defining and runing multiple-container Docker applications. It allows you to define a multi-container application in a single file, and then start and stop the entire application with a single command. 
Example:
```yaml
version: '3'

services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: "redis:alpine"

```
to run application
```cml
# Run application
docker-compose up

# Stop application
docker-compose down
```

## 2. Docker Networking
Dokcer Networkong allows you to create virtual networks that connect Docker containers. This is useful for isolating containers and providing communication betwwen them.
Example:
```
# Create a Docker network
docker netwok create my-network

# Start a container connected to the network
docker run --name container1 --network my-network my-image

# Start another container connected to the same network
docker run --name container2 --network my-network my-image
```
This above command help connect container1 and container2 via the my-network

## 3. Docker Volumes
Docker Volumes allow you to persist data from Docker containers to the host machine or to other containers.
Using for:
- Storing configuration files
- Databases
- Data that needs to persist even if the container is stopped or deleted
Example:
```
Copy code
# Create a Docker volume
docker volume create my-volume

# Start a container with the volume mounted
docker run --name container1 -v my-volume:/data my-image
```
with above command you can mount the '/data' to 'my-volume'

## 4. Docker Swarm
Docker Swarm is a toools for orchestrating Docker containers across mutiple hosts. It allows you create a cluster of Docker hosts and deploy applications to the cluster with ease.
Example:
```
# Initialize the Docker Swarm
docker swarm init

# Create a service to deploy the application
docker service create --replicas 3 --name my-service my-image

```
This command to create service that runs three replicas of the 'my-image'.
This service is automaticlly distributed across the Docker Swarn cluster
