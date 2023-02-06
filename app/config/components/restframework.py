REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "movies.api.v1.paginators.MyPaginator",
    "PAGE_SIZE": 50,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}
