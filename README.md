# Learning Docker
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

### Copy file / directory

