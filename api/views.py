from serializers import *
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework import generics
from rest_framework import filters
from rest_framework_gis.filters import DistanceToPointFilter


class CitiesListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    distance_filter_field = 'location'
    # How to filter
    filter_backends = (DistanceToPointFilter, filters.DjangoFilterBackend,)
    filter_fields = ('location', 'id')
    distance_filter_convert_meters = True


class CitiesDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class AppUserListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    distance_filter_field = 'location'
    # How to filter
    filter_backends = (DistanceToPointFilter, filters.DjangoFilterBackend,)
    filter_fields = ('location', 'id')
    distance_filter_convert_meters = True


class AppUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class FavoritesListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer


class FavoritesDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
