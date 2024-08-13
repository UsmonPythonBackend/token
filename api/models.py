from django.db import models
from .helpers import SaveMediaFiles

class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMediaFiles.save_artist_image)
    nick_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nick_name


class Albom(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMediaFiles.save_albom_image)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ['id']

class Songs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFiles.save_songs_image)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Meta:
    ordering = ['id']

class SongsAlbom(models.Model):
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Songs)