from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(UpVote)
admin.site.register(DownVote)
admin.site.register(Review)
admin.site.register(FavGenre)