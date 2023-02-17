from django_elasticsearch_dsl import Document, Index, fields
from movies.models import Filmwork

# Name of the Elasticsearch index
FILMWORK_INDEX = Index("filmwork")
# See Elasticsearch Indices API reference for available settings
FILMWORK_INDEX.settings(number_of_shards=1, number_of_replicas=1)


@FILMWORK_INDEX.doc_type
class FilmworkDocument(Document):
    """Publisher Elasticsearch document."""

    title = fields.TextField(
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        }
    )

    class Meta:
        """Meta options."""

        model = Filmwork  # The model associate with this Document
