# pull official base image

FROM python:3.10.12-alpine

# set work directory

WORKDIR /app/otcexchange

# set environment variables

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependancies

RUN apk update && apk add 'postgresql-dev' 'gcc' 'libffi-dev' 'python3-dev' 'musl-dev' 'build-base' 'py3-pip' 'zlib-dev' 'jpeg-dev' 'openssl-dev' 'gmp-dev'

# install package dependencies

COPY ./otcexchange/requirements.txt /app/otcexchange/requirements.txt
RUN python3 -m pip install setuptools wheel fastecdsa==2.3.2 && python3 -m pip install --upgrade pip setuptools wheel && python3 -m pip install -r /app/otcexchange/requirements.txt


# Copy the project
COPY ./otcexchange .
# RUN chmod +x /app/src/entrypoint.sh && chmod +x /app/src/start.sh

EXPOSE 8000

# ENTRYPOINT [ "/app/src/entrypoint.sh" ]
# CMD [ "/app/src/start.sh", "server" ]
