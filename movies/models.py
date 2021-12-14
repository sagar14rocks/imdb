from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class FavGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.genre.name


class Movie(models.Model):
    name = models.CharField(max_length=30)
    genres = models.ManyToManyField(Genre, related_name='movies')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    release_date = models.DateField()


    def __str__(self):
        return self.name

    def downvote_count(self):
        return DownVote.objects.filter(movie=self).count()

    def upvote_count(self):
        return UpVote.objects.filter(movie=self).count()


class Review(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class UpVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
   


class DownVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username


