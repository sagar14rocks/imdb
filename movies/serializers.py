from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

UserModel = get_user_model()


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("name",)


class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(read_only=True, many=True)
    upvotes = serializers.CharField(read_only=True, source='upvote_count')
    downvotes = serializers.CharField(read_only=True, source='downvote_count')

    class Meta:
        model = Movie
        fields = ( "id", "name", "release_date", "genres", "upvotes", "downvotes")

