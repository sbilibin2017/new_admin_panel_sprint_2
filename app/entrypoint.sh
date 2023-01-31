#!/bin/sh

# ждем подключение к БД
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi
exec "$@"



# создаем миграции
echo "\nCreating migrations..."
python3 manage.py makemigrations 

# список миграций
echo "\nMigrations list..."
python3 manage.py showmigrations 

echo "\nApplying migrations for django default tables..."
# применяем миграции
python3 manage.py migrate admin
python3 manage.py migrate auth
python3 manage.py migrate contenttypes
python3 manage.py migrate sessions

echo "\nApplying movies fake zero migration..."
# для movies делаем фейковую миграцию
python3 manage.py migrate --fake movies 0001
echo "Applying movies migrations..."
# для movies применяем оставшиеся миграции
python3 manage.py migrate movies

echo "\nCollecting static..."
# собираем статику
python3 manage.py collectstatic --noinput


echo "\nCreating superuser..."
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi
$@


# поднимаем сервер
echo "\nRunning django app with gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000




