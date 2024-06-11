# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim as base




WORKDIR /app

COPY ./requirements.txt /app/media/requirements.txt



RUN cd /app/media/ && pip install --no-cache-dir --upgrade -r /app/media/requirements.txt


COPY . ./app/media/



EXPOSE 8001


