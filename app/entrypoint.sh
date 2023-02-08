#!/bin/sh

# migrations
python3 manage.py migrate --fake 
# static
python3 manage.py collectstatic --noinput
# superuser
python3 manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL
# run server
gunicorn config.wsgi:application --bind 0.0.0.0:8000




