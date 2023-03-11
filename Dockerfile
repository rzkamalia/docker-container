# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
FROM ubuntu:20.04

ENV TZ="Asia/Jakarta"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update
RUN apt -y install pkg-config 
RUN apt -y install python3-dev python3-pip

RUN rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

RUN rm -f requirements.txt
RUN apt clean
RUN apt autoclean
RUN apt -y autoremove
RUN rm -rf ~/.local/share/Trash/*

CMD python3 /app/inference.py