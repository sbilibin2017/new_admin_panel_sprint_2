'''DRF предаставления.'''

from movies.api.v1.serializers import PersonSerializer
from movies.models import Person
from rest_framework import viewsets


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    '''API endpoint that allows users to be viewed or edited.'''

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
