from bo.models import *
from rest_framework import serializers

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
