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

netstat -tuln | grep 8765
lsof -i :8765

docker exec -it running-rev-deutsch /bin/bash

docker run -it --name running-rev-deutsch --rm -p EXTERNO:CONTENEDOR rev-deutsch
docker run -it --name running-rev-deutsch --rm -p 4433:8765 rev-deutsch

lsof -i :4433

docker run -d -p 127.0.0.1:8765:8765
docker run -it --name running-rev-deutsch --rm -p 127.0.0.1:8765:8765 rev-deutsch

información sobre la red de puente predeterminada de Docker:
docker network inspect bridge

Publicar la imagen
docker login
docker build -t rev-deutsch:1.0.1 .
docker tag rev-deutsch:1.0.0 revione/rev-deutsch:1.0.0
docker push revione/rev-deutsch:1.0.0

Crear un builder para linux/amd64:
docker buildx create --use
docker buildx inspect --bootstrap

Name: happy_hamilton
Driver: docker-container
Last Activity: 2024-02-20 20:01:43 +0000 UTC

Nodes:
Name: happy_hamilton0
Endpoint: desktop-linux
Status: running
Buildkit: v0.12.5
Platforms: linux/arm64, linux/amd64, linux/amd64/v2, linux/riscv64, linux/ppc64le, linux/s390x, linux/386, linux/mips64le, linux/mips64, linux/arm/v7, linux/arm/v6
Labels:
org.mobyproject.buildkit.worker.executor: oci
org.mobyproject.buildkit.worker.hostname: 999

docker buildx build --platform linux/amd64 -t rev-deutsch:1.0.0 --push .

docker build --platform linux/amd64 -t rev-deutsch:1.0.0 .
docker tag rev-deutsch:1.0.0 revione/rev-deutsch:1.0.0
docker push revione/rev-deutsch:1.0.0

docker build --platform linux/amd64 -t rev-deutsch:1.0.1 .
docker tag rev-deutsch:1.0.1 revione/rev-deutsch:1.0.1
docker push revione/rev-deutsch:1.0.1
