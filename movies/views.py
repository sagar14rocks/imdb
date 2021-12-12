from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MovieSerializer
from django.contrib.auth import authenticate
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from django.http import Http404
from .models import *
# from rest_framework.exceptions import ValueError




class MovieView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def get_object(self, id):
        try:
            return Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request):
        movie = self.get_object(request.data.get('id'))
        serializer = MovieSerializer(movie)
        return Response({"movie": serializer.data})


class VoteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        movie_id = request.data.get("movie_id")
        upvote = request.data.get("upvote")
        downvote = request.data.get("downvote")
        try:
            movie = Movie.objects.get(id=movie_id)
        except:
            return Response({"success": False, "message": "Movie not found"}, status=HTTP_404_NOT_FOUND)
        
        if upvote:
            if UpVote.objects.filter(user=request.user, movie=movie):
                return Response({"success": False, "message": "Already upvoted"}, status=HTTP_200_OK)
            else:
                UpVote.objects.create(user=request.user, movie=movie)
        if downvote:
            if DownVote.objects.filter(user=request.user, movie=movie):
                return Response({"success": False, "message": "Already downvoted"}, status=HTTP_200_OK)
            else:
                DownVote.objects.create(user=request.user, movie=movie)

        return Response({"success": True}, status=HTTP_200_OK)


class ReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        movie_id = request.data.get("movie_id")
        review = request.data.get("review")
        try:
            movie = Movie.objects.get(id=movie_id)
        except:
            return Response({"success": False, "message": "Movie not found"}, status=HTTP_404_NOT_FOUND)
        if review:
            Review.objects.create(title=review, user=request.user, movie=movie)
        return Response({"success": True}, status=HTTP_200_OK)

class FavGenreView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)