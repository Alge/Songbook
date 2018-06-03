from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from songbook.serializers import *
from .models import *
from django.http import HttpResponse
import json
from django_filters.rest_framework import DjangoFilterBackend


def add_song(request):

    if request.method != "POST":
        return HttpResponse("405, use POST requests")


    if not request.POST.get('data', False):
        return HttpResponse("Specify 'data'")


    try:
        data = json.loads(request.POST.get('data', False))

    except:
        return HttpResponse("Send valid JSON in 'data'")

    if not data.get("name", False):
        return HttpResponse("include 'name' in 'data'")

    if not data.get("text", False):
        return HttpResponse("include 'text' in 'data'")


    

    return HttpResponse(html)

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

    filter_backends = (DjangoFilterBackend,)

    filter_fields = ('name', 'category', 'melody', 'composer', 'author', )

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


class CollectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

