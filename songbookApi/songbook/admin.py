from django.contrib import admin

from .models import Writer, Song, Collection
# Register your models here.

admin.site.register(Writer)
admin.site.register(Song)
admin.site.register(Collection)
