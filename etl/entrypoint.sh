#!/bin/sh

# ждем подключение к БД

sleep 10 

python3 main.py

echo "Testing ..."
pytest tests/check_consistency/tests.py