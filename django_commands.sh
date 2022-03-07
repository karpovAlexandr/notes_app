#!/bin/sh

DOCKER_COMPOSE_FILE="docker-compose.yml"

docker-compose -f "$DOCKER_COMPOSE_FILE" exec web python manage.py collectstatic --noinput
docker-compose -f "$DOCKER_COMPOSE_FILE" exec web python manage.py migrate --noinput
docker-compose -f "$DOCKER_COMPOSE_FILE" exec web python manage.py