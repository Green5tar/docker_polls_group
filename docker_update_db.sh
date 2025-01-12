#!/bin/bash

docker-compose up -d
docker exec dpg_api python manage.py makemigrations authentication
docker exec dpg_api python manage.py migrate --noinput
docker-compose stop
