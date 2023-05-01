# docker

Build docker image for app:
```
docker build -t image_name:image_tag .
```

Pull image for database PostgreSQL:
```
docker pull postgres 
```
Running the postgres image:
```
docker run --name postgresql -p 8080:5432 -e POSTGRES_PASSWORD=yourpass postgres
```

Pull image for pgAdmin4:
```
docker pull dpage/pgadmin4
```
Running the pgadmin4 image:
```
docker run --name pgadmin -p 8081:80 -e "PGADMIN_DEFAULT_EMAIL=your.email@domain.com" -e "PGADMIN_DEFAULT_PASSWORD=yourpass" dpage/pgadmin4
```

Running the app image:
```
docker run --name app -p 5000:5000 image_name:image_tag
```

References:
1. [**Docker ubuntu installation tutorial.**](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
2. [**Docker image PostgreSQL.**](https://hub.docker.com/_/postgres)
3. [**Docker image pgAdmin4.**](https://hub.docker.com/r/dpage/pgadmin4/)
4. [**Docker engine networking ㅡ communicate between a container.**](https://docs.docker.com/network/network-tutorial-overlay/)
