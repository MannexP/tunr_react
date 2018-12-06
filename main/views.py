

from rest_framework import viewsets
from main.serializers import ArtistSerializer, SongSerializer
from main.models import Artist, Song


class ArtistView(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer