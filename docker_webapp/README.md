# Containerize simple web application

### Start all comtainers:
```sh
docker-compose up
```
### Check status of the container manager by docker compose:
```sh
docker-compose ps
```
### See logs:
```sh
docker-compose logs
```
### Output append logs:
```sh
 docker-compose logs -f
```
### Output specific container:
```sh
 docker-compose logs -f tareque20/webapp
```
### Stop running containers without removing:
```sh
 docker-compose stop
```
### Remove all containers:
```sh
 docker-compose rm
```
### Rebuild all the images:
```sh
 docker-compose build
```
