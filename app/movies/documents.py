from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from movies.models import Filmwork


@registry.register_document
class FilmworkDocument(Document):
    class Index:
        name = "filmworks"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Filmwork
        fields = [
            "title",
        ]
