from django.contrib.auth.models import User, Group
from songbook.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name', 'description')

class VerseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Verse
        fields = ('url', 'name', 'text', 'description', 'text', 'sorting_weight', 'song')

class SongSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Song
        fields = ('url', 'name', 'description', 'composer', 'arranger', 'original_text', 'new_text', 'added_by', 'category', 'verses')



class WriterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Writer
        fields = ('name', 'description')

class MelodySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Melody
        fields = ('name', 'description', 'link')