from rest_framework import serializers
from . import models


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actors
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Directors
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movies
        fields = '__all__'
