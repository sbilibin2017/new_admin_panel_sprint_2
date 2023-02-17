from django.conf.urls import re_path
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include("movies.api.urls")),
    re_path(r"^search/", include("search_indexes.urls")),
]
