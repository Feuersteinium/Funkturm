FROM alpine
MAINTAINER Niklas Feuerstein, <contact@feuerstein.dev>

# Install GIT
RUN apt add --no-cache git

# Add pull.sh and make it executable
COPY ./pull.sh /pull.sh
RUN chmod 777 /pull.sh

## Add user container
RUN adduser -D -h /home/web container
USER container
ENV  USER=container HOME=/home/container
WORKDIR /home/web

# CMD to run when starting the container
CMD ["bin/sh", "/pull.sh"]