import requests


def custom_show_toolbar(request: requests.models.Response) -> bool:
    '''Показывает панель дебага.'''
    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
}
