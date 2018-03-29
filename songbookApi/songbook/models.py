from django.db import models
from django.contrib.auth import get_user_model


class Writer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, default=None)


class Song(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.CharField(max_length=500, null=True, blank=True)
    composer        = models.ForeignKey(Writer, null=True, blank=True, on_delete=models.SET_NULL, related_name="composer")
    arranger        = models.ForeignKey(Writer, null=True, blank=True, on_delete=models.SET_NULL, related_name="arranger")
    original_text   = models.ForeignKey(Writer, null=True, blank=True, on_delete=models.SET_NULL, related_name="original_text")
    new_text        = models.ForeignKey(Writer, null=True, blank=True, on_delete=models.SET_NULL, related_name="new_text")
    text            = models.TextField()
    added_by        = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, blank=True)



class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    songs = models.ManyToManyField(Song)
    added_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, blank=True)

