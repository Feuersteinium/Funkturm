FROM alpine

MAINTAINER Niklas Feuerstein, <contact@feuerstein.dev>



# Installing Java and Python and Wget
RUN apk add --no-cache python3 openjdk17-jre-headless wget py3-pip

ADD requirements.txt /home/container/requirements.txt
RUN pip install -r /home/container/requirements.txt


# Adding User
RUN adduser -D -h /home/container container
ENV  USER=container HOME=/home/container
WORKDIR /home/container

# Adding Entrypoint
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


RUN echo test


# Done!
CMD ["/bin/sh", "/entrypoint.sh"]
