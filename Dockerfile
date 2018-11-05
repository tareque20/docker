FROM ubuntu
RUN apt-get update && apt-get install -y vim
ADD test.txt /var/html/test.txt
CMD ["echo", "Hello Tasfin"]