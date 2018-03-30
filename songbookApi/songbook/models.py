from django.db import models
from django.contrib.auth import get_user_model


class Writer(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.TextField(null=True, blank=True, default=None)
    def __str__(self):
        return 'Writer : ' + self.name

class Melody(models.Model):
    name            = models.CharField(max_length=200)
    description     = models.TextField()
    link            = models.URLField()

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
    category        = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    composer        = models.ForeignKey(Writer, null=True, blank=True, on_delete=models.SET_NULL, related_name="composer")
    arranger        = models.ForeignKey(Writer, null=True, blank=True, on_delete=models.SET_NULL, related_name="arranger")
    original_text   = models.ForeignKey(Writer, null=True, blank=True, on_delete=models.SET_NULL, related_name="original_text")
    new_text        = models.ForeignKey(Writer, null=True, blank=True, on_delete=models.SET_NULL, related_name="new_text")
    added_by        = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return 'Song: ' + self.name

class Collection(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.CharField(max_length=500, null=True, blank=True)
    songs           = models.ManyToManyField(Song)
    added_by        = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return 'Collection: ' + self.name

class Verse(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.CharField(max_length=500, null=True, blank=True)
    sorting_weight  = models.IntegerField()
    text            = models.TextField()
    song            = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='verses')

    def __str__(self):
        return 'Verse: (' + self.song.name + ')' + " : " + self.name