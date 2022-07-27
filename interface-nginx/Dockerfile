# Simple nginx image
FROM ubuntu
#ENV NGINX_VERSION 1.18-ubuntu20.04
RUN apt-get update && apt-get install -y curl
RUN apt-get update && apt-get install -y nginx

WORKDIR /interface-nginx
COPY index.html .

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

STOPSIGNAL SIGTERM 

HEALTHCHECK CMD curl localhost:80


