from requests import Response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import authentication
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializerWeb, AlbomSerializerWeb, SongsSerializerWeb, ArtistSerializerTelegram, AlbomSerializerTelegram, SongsSerializerTelegram


# Web
class ArtistViewSetWeb(viewsets.ModelViewSet):
    serializer_class = ArtistSerializerWeb
    permission_classes = [IsAuthenticated]
    autehntication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Artist.objects.all()


class AlbomViewSetWeb(viewsets.ModelViewSet):
    serializer_class = AlbomSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Albom.objects.all()


class SongsViewSetWeb(viewsets.ModelViewSet):
    serializer_class = SongsSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Songs.objects.all()


# Telegram
class ArtistViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = ArtistSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Artist.objects.all()


class AlbomViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = AlbomSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Albom.objects.all()


class SongsViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = SongsSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Songs.objects.all()





class TokenCheck(APIView):
    def get(self, request):
        from rest_framework.authtoken.models import Token

        token = Token.objects.create(user=request.user)
        print(token.key)
