#!/bin/sh

echo 'Waiting for postgres...'
sleep 1
echo 'PostgreSQL started'

python manage.py collectstatic --no-input
gunicorn config.wsgi:application --bind 0.0.0.0:8000




