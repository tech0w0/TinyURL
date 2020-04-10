
FROM ubuntu:latest

WORKDIR /lab1

COPY . /lab1

RUN apt-get update && apt-get install -y python3 
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev
RUN pip3 install pymongo
RUN pip3 install Flask
RUN pip3 install flask_pymongo

CMD flask run --host='0.0.0.0' --port=80