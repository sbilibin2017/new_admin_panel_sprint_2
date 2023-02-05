"""Django urls."""

from django.urls import include, path
from movies.api.v2 import views
from rest_framework import routers

urlpatterns = [
    path("movies/", views.MoviesListApi.as_view()),
    path("movies/<uuid:pk>/", views.MoviesDetailApi.as_view()),
]
