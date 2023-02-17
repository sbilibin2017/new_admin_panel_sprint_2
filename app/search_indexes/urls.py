from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .viewsets import FilmworkDocumentView

router = DefaultRouter()
filmworks = router.register(
    r"filmworks", FilmworkDocumentView, basename="filmworkdocument"
)

urlpatterns = [
    url(r"^", include(router.urls)),
]
