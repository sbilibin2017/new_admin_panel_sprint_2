"""Views."""

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import F, Q
from django.db.models.functions import Coalesce
from movies.api.v1.paginations import MoviesViewSetPaginator
from movies.api.v1.serializers import MoviesListSerializer
from movies.models import Filmwork
from rest_framework import filters, serializers, viewsets


class MoviesViewSet(viewsets.ReadOnlyModelViewSet):
    """View for list of movies with info about genres and persons."""

    # django model
    model = Filmwork
    # drf serializer
    serializer_class = MoviesListSerializer
    # pagination
    pagination_class = MoviesViewSetPaginator
    # search
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

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

    def add_actor_filter(self, queryset):
        person = self.request.query_params.get("actor")
        if person is not None:
            queryset = queryset.filter(actors__contains=[person])
        return queryset

    def add_director_filter(self, queryset):
        person = self.request.query_params.get("director")
        if person is not None:
            queryset = queryset.filter(directors__contains=[person])
        return queryset

    def add_writer_filter(self, queryset):
        person = self.request.query_params.get("writer")
        if person is not None:
            queryset = queryset.filter(writers__contains=[person])
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
            rating=Coalesce(F("rating"), float(0)),
            genres=ArrayAgg("genres__name", distinct=True, default=[]),
            actors=self.filter_role("actor"),
            directors=self.filter_role("director"),
            writers=self.filter_role("writer"),
        )
        queryset = self.add_genre_filter(queryset)
        queryset = self.add_actor_filter(queryset)
        queryset = self.add_director_filter(queryset)
        queryset = self.add_writer_filter(queryset)
        queryset = self.add_title_filter(queryset)

        return queryset
