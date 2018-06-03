from django.db import models
from django.contrib.auth import get_user_model


class Writer(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.TextField(null=True, blank=True, default=None)
    def __str__(self):
        return 'Writer : ' + self.name

class Melody(models.Model):
    name            = models.CharField(max_length=200)
    description     = models.TextField(null=True, blank=True)
    link            = models.URLField(null=True, blank=True)

    def __str__(self):
        return 'Melody: ' + self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return 'Category: ' + self.name

class Song(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.CharField(max_length=500, null=True, blank=True)
    melody          = models.ForeignKey(Melody, on_delete=models.SET_NULL, null=True, blank=True)
    category        = models.ManyToManyField(Category, blank=True)
    composer        = models.ManyToManyField(Writer, blank=True, related_name="composer")
    author   = models.ManyToManyField(Writer, blank=True, related_name="author")
    added_by        = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, blank=True)

    text            = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Song: ￼
￼
￼
Gilla
Kommentera
' + self.name

class Collection(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.CharField(max_length=500, null=True, blank=True)
    songs           = models.ManyToManyField(Song)
    added_by        = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return 'Collection: ' + self.name


class File(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=250)