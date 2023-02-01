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

python3 main.py

echo "Testing ..."
pytest tests/check_consistency/tests.py