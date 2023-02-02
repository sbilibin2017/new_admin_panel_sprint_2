'''DRF маршруты для api.'''

from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('movies.api.v1.urls')),
]
