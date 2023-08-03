FROM eclipse-temurin:20-jdk-alpine

MAINTAINER Niklas Feuerstein, <contact@feuerstein.dev>



# Installing Java and Python and Wget
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories && echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories && apk add --no-cache python3 wget py3-pip

ADD requirements.txt /home/container/requirements.txt
RUN pip install -r /home/container/requirements.txt --break-system-packages


# Adding User
RUN adduser -D -h /home/container container
USER container
ENV  USER=container HOME=/home/container
WORKDIR /home/container

# Adding Entrypoint
COPY ./entrypoint.sh /entrypoint.sh
RUN cd / && chmod +x entrypoint.sh

# Done!
CMD ["/bin/sh", "/entrypoint.sh"]
