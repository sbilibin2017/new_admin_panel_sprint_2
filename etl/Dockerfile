# версия питона
FROM python:3.10

# переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH "${PYTHONPATH}:/sqlite_to_postgres"

# рабочая директория
WORKDIR /sqlite_to_postgres

# устанавливаем netcat
RUN apt-get update && apt-get install -y netcat

COPY pyproject.toml .
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install 

# копируем код
COPY . .

# даем права на редактирование
RUN sed -i 's/\r$//g' /sqlite_to_postgres/entrypoint.sh
RUN chmod +x /sqlite_to_postgres/entrypoint.sh

# выполняем код в точке входа
ENTRYPOINT ["/sqlite_to_postgres/entrypoint.sh"]


