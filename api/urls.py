from django.urls import path, include
from rest_framework import routers
from .views import ArtistViewSetWeb, ArtistViewSetTelegram
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'artists-web', ArtistViewSetWeb, basename='artists-web')
router.register(r'artists-tele', ArtistViewSetTelegram, basename='artist-tele')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth-token/', obtain_auth_token),
]