from pathlib import Path

# корень проекта
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# директория со стотическими файлами
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'
