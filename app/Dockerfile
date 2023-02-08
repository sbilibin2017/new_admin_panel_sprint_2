# версия питона
FROM python:3.10

# переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE 'config.settings'
ENV APP /app
ENV GROUP django
ENV TZ=Europe/Moscow

RUN apt install tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc    

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system --dev

WORKDIR ${APP}

# копируем код
COPY . .

# даем права на редактирование
RUN chmod +x ${APP}/entrypoint.sh

# RUN groupadd -r ${GROUP} && useradd -d ${APP} -r -g ${GROUP} ${GROUP} \
#     && chown ${GROUP}:${GROUP} -R ${APP}
# USER ${GROUP}

# выполняем код в точке входа
ENTRYPOINT ["/app/entrypoint.sh"]


