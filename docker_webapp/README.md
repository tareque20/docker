# Containerize simple web application

### Build image:
```sh
docker build -t tareque20/webapp:1.0.0 .
```
### Check image:
```sh
docker images
```
### Run image:
```sh
docker run -d -p 5000:5000 image_id
```
### Check Docker image:
```sh
 docker ps
```
### Enter to image:
```sh
 docker exec -it container_id bash
```