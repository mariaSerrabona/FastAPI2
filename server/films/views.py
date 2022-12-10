from django.shortcuts import render
from rest_framework import viewsets
from .models import Film, FilmGenre
from .serializers import (FilmSerializer, FilmGenreSerializer,
                            FilmUserSerializer)

# Create your views here.

class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FilmGenre.objects.all()
    serializer_class = FilmGenreSerializer
    lookup_field = 'slug'  # identificaremos los géneros usando su slug
