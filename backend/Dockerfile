# pull official base image
FROM python:3.7.4-alpine

# set work directory
WORKDIR /var/www/binate/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

COPY requirements.txt /var/www/binate/backend/requirements.txt
WORKDIR /var/www/binate/backend
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# copy project
COPY . /var/www/binate/backend

