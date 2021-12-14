from django.urls import path
from .views import MovieView, VoteView, ReviewView, FavGenreView


urlpatterns = [
    path('', MovieView.as_view(), name='add_movie'),
    path('vote/', VoteView.as_view(), name='vote'),
    path('review/', ReviewView.as_view(), name='review'),
    path('favgenre/', FavGenreView.as_view(), name='favgenre'),
]
