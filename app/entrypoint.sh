#!/bin/sh

echo 'Waiting for postgres...'
sleep 1
echo 'PostgreSQL started'

python3 manage.py migrate --no-input
python manage.py collectstatic --no-input

echo 'Setting Django admin ...'
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi
$@

echo 'Running django admin ...'
gunicorn config.wsgi:application --bind 0.0.0.0:8000




