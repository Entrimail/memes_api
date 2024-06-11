# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim as base




WORKDIR /app

COPY ./requirements.txt /app/api/requirements.txt

RUN cd /app/api/ && pip install --no-cache-dir --upgrade -r /app/api/requirements.txt

COPY . ./app/api/





EXPOSE 8000


