FROM alpine
MAINTAINER Niklas Feuerstein, <contact@feuerstein.dev>

# Install GIT
RUN apk add --no-cache git nginx

# Add pull.sh and make it executable
COPY ./nginx.conf /app/nginx.conf
COPY ./pull.sh /pull.sh
RUN chmod 777 /pull.sh

## Add user container
RUN adduser -D -h /home/web container
USER container
ENV  USER=container HOME=/home/app
WORKDIR /home/app

# CMD to run when starting the container
CMD ["bin/sh", "/pull.sh"]