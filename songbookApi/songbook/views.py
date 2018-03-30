from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from songbook.serializers import *
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows songs to be viewed or edited.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class VerseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows verses to be viewed or edited.
    """
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer

class WriterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows writers to be viewed or edited.
    """
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MelodyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Melody.objects.all()
    serializer_class = MelodySerializer


