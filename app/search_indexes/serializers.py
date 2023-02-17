from django_elasticsearch_dsl_drf import serializers

from .documents import FilmworkDocument


class FilmworkDocumentSerializer(serializers.DocumentSerializer):
    """Serializer for Publisher document."""

    class Meta:
        """Meta options."""

        model = FilmworkDocument
        # Note, that since we're using a dynamic serializer,
        # we only have to declare fields that we want to be shown. If
        # somehow, dynamic serializer doesn't work for you, either extend
        # or declare your serializer explicitly.
        fields = ("title",)
