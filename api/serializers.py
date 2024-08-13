# Web Application
# Telegram API
from rest_framework import serializers
from api.models import Artist, Albom, Songs, SongsAlbom


# Web
class ArtistSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'first_name', 'last_name', 'nick_name', 'image')

class AlbomSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ('id','title', 'artist', 'description')

class SongsSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('id', 'title', 'artis', 'description')

class SongsAlbomSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = SongsAlbom
        fields = ('id', 'artist', 'songs')

#Telegram
class ArtistSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'nick_name', 'image')

class AlbomSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ('title', 'description')

class SongsSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('title', 'artis', 'description')

