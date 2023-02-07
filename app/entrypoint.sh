#!/bin/sh

# ждем подключение к БД
sleep 1 

# список миграций
echo "\nMigrations list..."
python3 manage.py showmigrations 

echo "Applying migrations..."
# применяем миграции
python3 manage.py migrate --fake 

echo "\nCollecting static..."
# собираем статику
python3 manage.py collectstatic --noinput


echo "\nCreating superuser..."
python3 manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL


# поднимаем сервер
echo "\nRunning django app with gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000




