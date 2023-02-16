import os

ELASTICSEARCH_DSL = {
    "default": {"hosts": os.getenv("ELASTICSEARCH_DSL_HOSTS", "localhost:9200")},
}
