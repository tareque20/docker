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

# Dockerfile:

```js
# creates a layer from the node:carbon Docker image
FROM node:carbon
# create the app directory for inside the Docker image
WORKDIR /usr/src/app
# copy and install app dependencies from the package.json (and the package-lock.json) into the root of the directory created above
COPY package*.json ./
RUN npm install
# bundle app source inside Docker image
COPY . .
# expose port 8080 to have it mapped by Docker daemon
EXPOSE 8080
# define the command to run the app (it's the npm start script from the package.json file)
CMD [ "npm", "start" ]
```


## Dockerfile:
 -  `FROM`: Sets the Base Image for subsequent instructions. 
	 - **Usage:**
		 - `FROM <image>`
		 - `FROM <image>:<tag>`
		 - `FROM <image>@<digest>`
		 
	- **Information:**
		-   `FROM`  must be the first non-comment instruction in the Dockerfile.
		-   `FROM`  can appear multiple times within a single Dockerfile in order to create multiple images. Simply make a note of the last image ID output by the commit before each new  `FROM`  command.
		-   The  `tag`  or  `digest`  values are optional. If you omit either of them, the builder assumes a  `latest`  by default. The builder returns an error if it cannot match the  `tag`  value.
 
-  `MAINTAINER`: Set the Author field of the generated images. Usage: `MAINTAINER <name>`

-  `ENV`: Sets environment variable. 
	- **Usage:**
		-   `ENV <key> <value>`
		-   `ENV <key>=<value> [<key>=<value> ...]`
	- **Information:**
		-   The  `ENV`  instruction sets the environment variable  `<key>`  to the value  `<value>`.
		-   The value will be in the environment of all “descendant” Dockerfile commands and can be replaced inline as well.
		-   The environment variables set using  `ENV`  will persist when a container is run from the resulting image.
		-   The first form will set a single variable to a value with the entire string after the first space being treated as the  `<value>`  - including characters such as spaces and quotes.
-  `LABEL`
	- **Usage:**
		- `LABEL <key>=<value> [<key>=<value> ...]`
	- **Information:**
		-   The  `LABEL`  instruction adds metadata to an image.
		-   To include spaces within a  `LABEL`  value, use quotes and backslashes as you would in command-line parsing.
		-   Labels are additive including  `LABEL`s in  `FROM`  images.
		-   If Docker encounters a label/key that already exists, the new value overrides any previous labels with identical keys.
		-   To view an image’s labels, use the  `docker inspect`  command. They will be under the  `"Labels"`  JSON attribute.

-  `RUN`: Execute any commands in a new layer on top of the current image and commit the results. 
	- **Usage:** 
		-  `RUN <command>`  (shell form, the command is run in a shell, which by default is  `/bin/sh -c`  on Linux or  `cmd /S /C`  on Windows)
		-   `RUN ["<executable>", "<param1>", "<param2>"]`  (exec form)
	- **Information:**
		- The exec form makes it possible to avoid shell string munging, and to  `RUN`  commands using a base image that does not contain the specified shell executable.
		-   The default shell for the shell form can be changed using the  `SHELL`  command.
		-   Normal shell processing does not occur when using the exec form. For example,  `RUN ["echo", "$HOME"]`  will not do variable substitution on  `$HOME`.

-  `CMD`: Specifies the command to run when a container is launched. It is similar to the `RUN` instruction, but rather than running the command when the container is being built, it will specify the command to run when the container is launched, much like specifying a command to run when launching a container with the `docker run` command. There can only be one `CMD` instruction in a `Dockerfile`. 
	- **Usage:** 
		- `CMD ["<executable>","<param1>","<param2>"]`  (exec form, this is the preferred form)
		-   `CMD ["<param1>","<param2>"]`  (as default parameters to ENTRYPOINT)
		-   `CMD <command> <param1> <param2>`  (shell form)
	- **Information:**
		-   The main purpose of a  `CMD`  is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an  `ENTRYPOINT`  instruction as well.
		-   There can only be one  `CMD`  instruction in a Dockerfile. If you list more than one  `CMD`  then only the last  `CMD`  will take effect.
		-   If  `CMD`  is used to provide default arguments for the  `ENTRYPOINT`  instruction, both the  `CMD`  and  `ENTRYPOINT`  instructions should be specified with the JSON array format.
		-   If the user specifies arguments to  `docker run`  then they will override the default specified in  `CMD`.
		-   Normal shell processing does not occur when using the exec form. For example,  `CMD ["echo", "$HOME"]`  will not do variable substitution on  `$HOME`.

-  `ENTRYPOINT`: We can override the `CMD` instruction on the `docker run` command line. The `ENTRYPOINT` instruction provides a command that isn’t as easily overridden. Instead, any arguments we specify on the `docker run` command line will be passed as arguments to the command specified in the `ENTRYPOINT`. 
	- **Usage:**
		-   `ENTRYPOINT ["<executable>", "<param1>", "<param2>"]`  (exec form, preferred)
		-   `ENTRYPOINT <command> <param1> <param2>`  (shell form)
	- **Information:**
		-   Allows you to configure a container that will run as an executable.
		-   Command line arguments to  `docker run <image>`  will be appended after all elements in an exec form  `ENTRYPOINT`  and will override all elements specified using  `CMD`.
		-   The shell form prevents any  `CMD`  or run command line arguments from being used, but the  `ENTRYPOINT`  will start via the shell. This means the executable will not be PID 1 nor will it receive UNIX signals. Prepend  `exec`  to get around this drawback.
		-   Only the last  `ENTRYPOINT`  instruction in the Dockerfile will have an effect.

-  `EXPOSE`: Informs Docker that the container listens on the specified network ports at runtime. It does not actually publish the port. Usage: `EXPOSE <port> [<port>...]`

-  `WORKDIR`: Sets the working directory for the container. 
	- **Usage:** 
		-   `WORKDIR </path/to/workdir>`
	- **Information:**
		-   Sets the working directory for any  `RUN`,  `CMD`,  `ENTRYPOINT`,  `COPY`, and  `ADD`  instructions that follow it.
		-   It can be used multiple times in the one Dockerfile. If a relative path is provided, it will be relative to the path of the previous  `WORKDIR`  instruction.

-  `VOLUME` Adds volumes to any container. Volumes can be shared and reused between containers. A container doesn’t have to be running to share its volumes. Usage: `VOLUME ["/data"]`

-  `ADD`: Copies new files, directories or remote file to container. 
	- **Usage:** 
		- `ADD <src> [<src> ...] <dest>`
		-   `ADD ["<src>", ... "<dest>"]`  (this form is required for paths containing whitespace)
	- **Information:**
		-   Copies new files, directories, or remote file URLs from  `<src>`  and adds them to the filesystem of the image at the path  `<dest>`.
		-   `<src>`  may contain wildcards and matching will be done using Go’s filepath.Match rules.
		-   If  `<src>`  is a file or directory, then they must be relative to the source directory that is being built (the context of the build).
		-   `<dest>`  is an absolute path, or a path relative to  `WORKDIR`.
		-   If  `<dest>`  doesn’t exist, it is created along with all missing directories in its path.

-  `COPY`: This is closely related to the `ADD` instruction. The key difference is that the `COPY` instruction is purely focused on copying local files from the build context and does not have any extraction or decompression capabilities. 
	- **Usage:** 
		-   `COPY <src> [<src> ...] <dest>`
		-   `COPY ["<src>", ... "<dest>"]`  (this form is required for paths containing whitespace)
	- **Information:**
		-   Copies new files or directories from  `<src>`  and adds them to the filesystem of the image at the path  `<dest>`.
		-   `<src>`  may contain wildcards and matching will be done using Go’s filepath.Match rules.
		-   `<src>`  must be relative to the source directory that is being built (the context of the build).
		-   `<dest>`  is an absolute path, or a path relative to  `WORKDIR`.
		-   If  `<dest>`  doesn’t exist, it is created along with all missing directories in its path.

-  `USER`: Specifies a user that the image should be run as; Usage: -   `USER <username | UID>`. The  `USER`  instruction sets the user name or UID to use when running the image and for any  `RUN`,  `CMD`  and  `ENTRYPOINT`  instructions that follow it in the Dockerfile.

-  `ARG`: Defines variables that can be passed at build-time via the `docker build` command. This is done using the `--build-arg <varname>=<value>` flag. Usage: `ARG <name>[=<default value>]`
- `HEALTHCHECK`
	- Usage:
		-   `HEALTHCHECK [<options>] CMD <command>`  (check container health by running a command inside the container)
		-   `HEALTHCHECK NONE`  (disable any healthcheck inherited from the base image)
	- **Information:**
		-   Tells Docker how to test a container to check that it is still working
		-   Whenever a health check passes, it becomes  `healthy`. After a certain number of consecutive failures, it becomes  `unhealthy`.
		-   The  `<options>`  that can appear are...
		    -   `--interval=<duration>`  (default: 30s)
		    -   `--timeout=<duration>`  (default: 30s)
		    -   `--retries=<number>`  (default: 3)
		-   The health check will first run  `interval`  seconds after the container is started, and then again  `interval`  seconds after each previous check completes. If a single run of the check takes longer than  `timeout`  seconds then the check is considered to have failed. It takes  `retries`  consecutive failures of the health check for the container to be considered  `unhealthy`.
		-   There can only be one  `HEALTHCHECK`  instruction in a Dockerfile. If you list more than one then only the last  `HEALTHCHECK`  will take effect.
		-   `<command>`  can be either a shell command or an exec JSON array.
		-   The command's exit status indicates the health status of the container.
		    -   `0`: success - the container is healthy and ready for use
		    -   `1`: unhealthy - the container is not working correctly
		    -   `2`: reserved - do not use this exit code
		-   The first 4096 bytes of stdout and stderr from the  `<command>`  are stored and can be queried with  `docker inspect`.
		-   When the health status of a container changes, a  `health_status`  event is generated with the new status.

# Some Tags:
## Networks:
> https://medium.com/@caysever/docker-compose-network-b86e424fad82
> https://docker-k8s-lab.readthedocs.io/en/latest/docker/docker-compose.html

## Volumes
> https://www.linux.com/learn/docker-volumes-and-networks-compose
> https://storidge.com/docs/volumes-docker-compose/


# docker-compose
```sh
version: "2"

services:
  voting-app:
    build: ./voting-app/.
    volumes:
     - ./voting-app:/app
    ports:
      - "5000:80"
    links:
      - redis
    networks:
      - front-tier
      - back-tier

  result-app:
    build: ./result-app/.
    volumes:
      - ./result-app:/app
    ports:
      - "5001:80"
    links:
      - db
    networks:
      - front-tier
      - back-tier

  worker:
    build: ./worker
    links:
      - db
      - redis
    networks:
      - back-tier

  redis:
    image: redis
    ports: ["6379"]
    networks:
      - back-tier

  db:
    image: postgres:9.4
    volumes:
      - "db-data:/var/lib/postgresql/data"
    networks:
      - back-tier

volumes:
  db-data:

networks:
  front-tier:
  back-tier:
```  