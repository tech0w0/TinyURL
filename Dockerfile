
FROM alpine:latest

WORKDIR /lab1

COPY . /lab1

RUN apk upgrade --no-cache 
RUN apk add --no-cache \
	python3 \
	python3-dev \
    && pip3 install --no-cache-dir --upgrade pip \
    && rm -rf /var/cache/* \
    && rm -rf /root/.cache/*
 

RUN cd /usr/bin \
  # && ln -sf easy_install-3.5 easy_install \
  && ln -sf python3 python \
  && ln -sf pip3 pip

RUN pip3 install pymongo
RUN pip3 install Flask
RUN pip3 install flask_pymongo
RUN pip3 install python-dotenv

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

CMD flask run --host='0.0.0.0' --port=80
