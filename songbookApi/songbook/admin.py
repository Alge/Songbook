from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Writer)
admin.site.register(Song)
admin.site.register(Collection)
admin.site.register(Melody)
admin.site.register(Category)
admin.site.register(Verse)

