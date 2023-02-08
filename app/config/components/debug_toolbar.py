import requests
from config.settings import DEBUG


def custom_show_toolbar(request: requests.models.Response) -> bool:
    '''Показывает панель дебага.'''
    return True


if bool(int(DEBUG)):
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    }
