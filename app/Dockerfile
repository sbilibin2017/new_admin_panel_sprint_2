# версия питона
FROM python:3.10

# переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE 'config.settings'


ENV TZ=Europe/Moscow
RUN apt install tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y --no-install-recommends gcc


WORKDIR /app

# копируем код
COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt    

# даем права на редактирование
RUN chmod +x /app/entrypoint.sh

RUN groupadd -r django && useradd -d /app -r -g django django \
    && chown django:django -R /app
USER django

# выполняем код в точке входа
ENTRYPOINT ["/app/entrypoint.sh"]


