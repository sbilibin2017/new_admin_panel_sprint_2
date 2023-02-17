from django_elasticsearch_dsl_drf.constants import LOOKUP_FILTER_GEO_DISTANCE
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
# Example app models
from search_indexes.documents import FilmworkDocument
from search_indxes.serializers import FilmworkDocumentSerializer


class PublisherDocumentView(DocumentViewSet):
    """The PublisherDocument view."""

    document = FilmworkDocument
    serializer_class = FilmworkDocumentSerializer
    lookup_field = "id"
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = ("title",)
    # Define filtering fields
    filter_fields = {
        "id": None,
        "title": "title.raw",
    }
    # Define ordering fields
    ordering_fields = {
        "id": None,
        "title": None,
        "city": None,
        "country": None,
    }
    # Specify default ordering
    ordering = (
        "id",
        "name",
    )
    # Define geo-spatial filtering fields
    geo_spatial_filter_fields = {
        "location": {
            "lookups": [
                LOOKUP_FILTER_GEO_DISTANCE,
            ],
        },
    }
