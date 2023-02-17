import os
from pathlib import Path

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

# корень проекта
BASE_DIR = Path(__file__).resolve().parent.parent
# загрузка переенных окружения
load_dotenv(BASE_DIR / ".env")
APP_NAME = os.getenv("APP_NAME")


class MoviesConfig(AppConfig):
    """App config."""

    default_auto_field = "django.db.models.BigAutoField"

    name = APP_NAME
    verbose_name = _(APP_NAME)

    def ready(self):
        pass
