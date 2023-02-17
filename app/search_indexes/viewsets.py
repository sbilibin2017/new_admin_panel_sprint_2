from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet

from .documents import FilmworkDocument
from .serializers import FilmworkDocumentSerializer


class FilmworkDocumentView(BaseDocumentViewSet):
    """The BookDocument view."""

    document = FilmworkDocument
    serializer_class = FilmworkDocumentSerializer
    pagination_class = PageNumberPagination
    lookup_field = "title"
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = ("title",)
    # Define filter fields
    filter_fields = {
        "title": "title.raw",
    }
