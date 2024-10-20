build image:
docker build -t rev-deutsch .

run
docker run -it --name running-rev-deutsch --rm -p 8765:8765 rev-deutsch
docker run -it --name running-rev-deutsch --rm -d -p 8765:8765 rev-deutsch
docker exec -it running-rev-deutsch /bin/bash

eliminar imagenes:

docker images

docker rmi rev-deutsch

docker rmi ID_de_la_imagen

eliminar containers:
docker ps

docker rm running-rev-deutsch

Verificar puerto:
lsof -i :8765

conjunto de docker:
docker rm running-rev-deutsch
docker rmi rev-deutsch
docker build -t rev-deutsch .
docker run -it --name running-rev-deutsch -d -p 8765:8765 rev-deutsch
docker run -it --name running-rev-deutsch --rm -d -p 8765:8765 rev-deutsch

probando el puerto del docker:
lsof -i :8765
apt-get update
apt-get install lsof

Verificar la Escucha del Servidor:
netstat -tuln | grep 8765

Logs del Contenedor:
docker logs running-rev-deutsch

stop container:
docker stop nombre_del_contenedor
docker stop running-rev-deutsch

otro conjunto:
docker stop running-rev-deutsch
docker rm running-rev-deutsch
docker rmi rev-deutsch
docker build -t rev-deutsch .
docker run -it --name running-rev-deutsch --rm -p 8765:8765 rev-deutsch
