# Cheatsheet of Docker and Docker Compose
## Docker Hub
| CMD                        | Description                          |
|----------------------------|-------------------------------------|
| `docker search searchterm` | Search Docker Hub for images.       |
| `docker pull user/image`   | Downloads an image from Docker Hub. |
|`docker login`              | Authenticate to Docker Hub (or other Docker registry).|
|`docker push user/image`    | Uploads an image to Docker Hub. You must be authenticated to run this command.|
|`docker create [image]`|Create a new container from a particular image.|

## Running Docker Containers
| CMD                        | Description                          |
|----------------------------|-------------------------------------|
| `docker start [container name or ID]` | Start a container.       |
| `docker stop [container name or ID]` | Stop a container.       |
| `docker exec -it [container name or ID] [command]` | Run a shell command inside a particular container.        |   
| `docker exec -it [container name or ID] bash`| ssh to the container |
| `docker run -it user/image` | Runs an image, creating a container and changing the terminal  to the terminal within the container.       |  
| `docker run -p $HOSTPORT:$CONTAINERPORT --name CONTAINER -d user/image` | Run an image in detached mode with port forwarding.       |            
| `docker run -it — image [image] [container] [command]` | Create and start a container at the same time, and then run a command inside it.       |         
| `docker attach [container name or ID]` | Changes the command prompt from the host to a running container.       |         
| `docker rm -f [container name or ID]` | Delete a container.       |         
| `docker rmi` |  Delete an image.      |         
| `docker tag user/image:tag user/image:newtag` | Add a new tag to an image.       |
| `docker kill $(docker ps -q)` |  Kill running containers      |
| `docker rm -f $(docker ps -qa)` |  Delete all containers (force!! running or stopped containers)      |   
| `docker ps -a | grep 'weeks ago' | awk '{print $1}' | xargs docker rm` | Delete old containers       |   
| `docker rm -v $(docker ps -a -q -f status=exited)` | Delete stopped containers      |   
| `docker stop $(docker ps -aq) && docker rm -v $(docker ps -aq)` | Delete containers after stopping      |   
| `docker rmi $(docker images -q -f dangling=true)` | Delete dangling images      |   
| `docker rmi $(docker images -q)` | Delete all images       |   

## Image Creation
| CMD                        | Description                          |
|----------------------------|-------------------------------------|
| `docker commit user/image` |  Save a container as an image.      |   
| `docker save user/image` |   Save an image to a tar archive.     |   
| `docker build -t sampleuser/ubuntu .` |  Builds a Docker image from a Dockerfile in the current directory.      |   
| `docker load` |  Loads an image from file.      |   

## Image and Container Information
| CMD                        | Description                          |
|----------------------------|-------------------------------------|
| `docker ps` | List all running containers.       |   
| `docker ps -a` | List all container instances, with their ID and status       |   
| `docker images` | Lists all images on the local machine.       |   
| `docker history user/image` | Lists the history of an image.       |   
| `docker logs [container name or ID]` | Displays the logs from a running container. |
| `docker port [container name or ID]` | Displays the exposed port of a running container. |
| `docker diff [container name or ID]` | Lists the changes made to a container. |
| `docker inspect [object]` | Display low-level information about a particular Docker object. |
| `docker version` |Display the version of Docker that is currently installed on the system.  |

# Docker Compose
## Docker Compose Commands
| CMD                        | Description                          |
|----------------------------|-------------------------------------|
| `docker-compose up -d` | start containers in background |  
| `docker-compose up -d --build` |force rebuild of Dockerfiles |
| `docker-compose ps` | see list of running containers |
| `docker-compose start` |Starts existing containers for a service. |
| `docker-compose inspect` | Display low-level information |	
| `docker-compose logs` | Show logs|
| `Docker-compose logs -f` | Follow the logs tail |
| `docker-compose stop` | Stops running containers without removing them. |
| `docker-compose kill` | stop containers |
| `docker-compose down` | Stops containers and removes containers, networks, volumes, and images created by up. |
| `docker-compose rm` | remove stopped containers |
 
	
# Example
```sh
docker run busybox:1.29 echo "Hello Tasfin"
docker run busybox:1.29 ls /
docker run -i -t busybox:1.29
```

### Detach mode:
```sh
docker run -d busybox:1.29 sleep 1000
```
### Remove Docker
```sh
docker run --rm busybox:1.29 sleep 1 // after 1 sec docker will remove
```
### Rename docker:
```sh
docker run --name tasfin busybox:1.29
```

### Inspect:
```sh
Run docker: docker run -d busybox:1.29 sleep 1000
docker inspect docker_logn_id
```
```sh
docker ps
docker ps -a
```
### Expose port:
```sh
docker run -d -p 8888:8080 tomcat:8.0
```
### Docker port:
```sh
docker port busybox:1.29
```
### See Logs:
```sh
docker logs docker_long_id
```
### Build Image:
```sh
docker build -t tareque20/ubuntu .
```
### Commit the changes:
```sh
docker commit docker_short_id tareque20/ubuntu:1.0.0
```
### Added TAG
```sh
docker tag docker_short_id tareque20/ubuntu:1.0.0
```
### Login to Docker Hub
```sh
docker login --username=tareque20
```
### Push Image to Docker Hub
```sh
docker push tareque20/ubuntu:1.0.0
```
### Logout from the Docker Hub
```sh
docker logout
```
### Delete Image
```sh
docker rmi tareque20/ubuntu:1.0.0
```