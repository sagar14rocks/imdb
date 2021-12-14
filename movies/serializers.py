from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

UserModel = get_user_model()


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("name",)


class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True)
    upvotes = serializers.CharField(read_only=True, source='upvote_count')
    downvotes = serializers.CharField(read_only=True, source='downvote_count')

    class Meta:
        model = Movie
        fields = ( "id", "name", "release_date", "genres", "upvotes", "downvotes")

    def create(self, validated_data):
        genres = validated_data.pop('genres')
        movie = Movie.objects.create(**validated_data)
        genre_names = []
        for genre in genres:
            genr, _ = Genre.objects.get_or_create(**genre)
            genre_names.append(genr.name)
        genre_ids = Genre.objects.filter(name__in=genre_names).values_list('id', flat=True)
        movie.genres.set(genre_ids)                    
        return movie

class FavGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavGenre
        fields = ("genre", "user",)