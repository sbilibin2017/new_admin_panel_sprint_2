'''DRF сериализаторы апи 1ой версии.'''

from movies.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    '''Сериализатор персон.'''

    class Meta:
        model = Person
        fields = '__all__'
