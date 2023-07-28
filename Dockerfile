# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
FROM ubuntu:20.04

ENV TZ="Asia/Jakarta"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update
RUN apt -y install pkg-config 
RUN apt -y install python3-dev python3-pip
RUN apt -y install libgl1

RUN mkdir /app
WORKDIR /app
COPY /dist /app

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install opencv-python
RUN pip3 install -r requirements.txt

RUN rm -f requirements.txt

CMD python3 /app/inference.py