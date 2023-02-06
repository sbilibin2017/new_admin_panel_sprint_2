"""Views."""

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import F, Q
from django.db.models.functions import Coalesce
from movies.api.v1.serializers import MoviesListSerializer
from movies.models import Filmwork
from rest_framework import serializers, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class MoviesViewSet(viewsets.ReadOnlyModelViewSet):
    """View for list of movies with info about genres and persons."""

    # django model
    model = Filmwork
    # drf serializer
    serializer_class = MoviesListSerializer
    # authatication
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def filter_role(self, role):
        """Filter person with role type."""
        return ArrayAgg(
            "persons__full_name",
            distinct=True,
            filter=Q(filmworkperson__role=role),
            default=[],
        )

    def add_genre_filter(self, queryset):
        genre = self.request.query_params.get("genre")
        if genre is not None:
            queryset = queryset.filter(genres__contains=[genre])
        return queryset

    def add_title_filter(self, queryset):
        title = self.request.query_params.get("title")
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def get_queryset(self):
        """Build queryset."""
        queryset = self.model.objects.values(
            "id", "title", "description", "creation_date", "type"
        ).annotate(
            rating=Coalesce(F("rating"), 0.0),
            genres=ArrayAgg("genres__name", distinct=True, default=[]),
            actors=self.filter_role("actor"),
            directors=self.filter_role("director"),
            writers=self.filter_role("writer"),
        )
        queryset = self.add_genre_filter(queryset)
        queryset = self.add_title_filter(queryset)

        return queryset
