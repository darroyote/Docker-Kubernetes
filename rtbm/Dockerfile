# OS base image.
FROM python:3.6-alpine AS os-base
RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev && \
    apk add --no-cache mariadb-dev

# Application base image.
FROM os-base AS app-base
ADD requirements.txt /opt
RUN pip install -r /opt/requirements.txt && \
    rm /opt/requirements.txt && \
    apk del .build-deps

# Application image.
FROM app-base
ARG SERVER_PORT=8080
ENV SERVER_PORT ${SERVER_PORT}

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=db
#ENV MYSQL_USER=user
#ENV MYSQL_PASSWORD=primera
ENV DB_HOST=172.17.0.2
ENV MYSQL_USER=root
ENV MYSQL_ALLOW_EMPTY_PASSWORD=True

ADD src /opt/src
EXPOSE ${SERVER_PORT}
ENTRYPOINT gunicorn --bind 0.0.0.0:${SERVER_PORT} \
                    --timeout 0 \
                    --workers 3 \
                    --worker-class eventlet \
                    --chdir /opt/src \
                    wsgi:flaskapp
