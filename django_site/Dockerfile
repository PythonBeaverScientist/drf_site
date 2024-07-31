FROM python:3.10

WORKDIR $DJANGO_ROOT

RUN apt update && apt install -y python3-pip libpq-dev python3-dev
RUN python3 -m pip install --upgrade pip poetry

COPY pyproject.toml poetry.lock ./
RUN python3 -m poetry install

COPY . .
ENV DJANGO_PORT=$DJANGO_PORT
ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]