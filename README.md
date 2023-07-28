# docker

In this repository, i am obfuscate the python script before build docker image.

Obfuscate the python script:
```
pyarmor-7 obfuscate inference.py
```
You can see the result in folder **/dist**. 

**Note**: i am using pyarmor version 8.2.8. If you use pyarmor version > 8.0.0 but only use old features, use pyarmor-7 instead of pyarmor (*see references in the last section for more info*).    

<br />

## build docker image for app
If **you not obfuscating your python script**, 
1. replace **COPY /dist /app** with **COPY . /app** in file **Dockerfile**.
1. add **running_docker/** in the last line in file **.dockerignore**. 

After that, build the docker image with the following command:
```
docker build -t image_name:image_tag .
```
If **you obfuscating your python script**, you directly run the command above without replace or add anything in any file.

<br />

## pull and run docker image for PostgreSQL
Pull image for database PostgreSQL:
```
docker pull postgres 
```
Running the postgres image:
```
docker run --name postgresql -p 8080:5432 -e POSTGRES_PASSWORD=yourpass postgres
```

<br/>

## pull and run docker image for pgAdmin4
Pull image for pgAdmin4:
```
docker pull dpage/pgadmin4
```
Running the pgadmin4 image:
```
docker run --name pgadmin -p 8081:80 -e "PGADMIN_DEFAULT_EMAIL=your.email@domain.com" -e "PGADMIN_DEFAULT_PASSWORD=yourpass" dpage/pgadmin4
```

<br/>

## run docker image for app
First, you should inside folder **runnning_docker** with the following command:
```
cd running_docker/
```
Make sure in file **config.cfg**, weight and connection database that you used are correct. 

Make sure in file **docker-compose.yaml**, image, volumes file config, volumes folder weights and ports that you used are correct.

After that, running the app image:
```
docker compose up -d
```

References:
1. [**Pyarmor.**](https://github.com/dashingsoft/pyarmor)
1. [**Docker ubuntu installation tutorial.**](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
1. [**Docker image PostgreSQL.**](https://hub.docker.com/_/postgres)
1. [**Docker image pgAdmin4.**](https://hub.docker.com/r/dpage/pgadmin4/)
1. [**Docker engine networking ㅡ communicate between a container.**](https://docs.docker.com/network/network-tutorial-overlay/)
