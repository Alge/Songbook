import json

import os

from django.core.management.base import BaseCommand
from songbook.models import Writer, Category, Melody, Song


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'


    def _create_writer(self, name, description=None):

        w = Writer()
        w.name = name
        w.description = description
        w.save()

        print("Created writer: {}".format(w))
        return w

    def _create_category(self, name, description=None):

        c = Category()
        c.name = name
        c.description = description
        c.save()
        return c

    def _create_melody(self, name, description=None, link=None):
        m = Melody()
        m.name = name
        m.description = description
        m.link = link
        m.save()
        return m

    def _create_song(self, song):
        s = Song()

        s.name = song["name"]

        s.text = song["text"]

        s.save()

        if "description" in song:
            s.description = song["description"]

        if "melody" in song:

            melody = Melody.objects.filter(name__iexact = song["melody"]).first()
            if not melody:
                melody = self._create_melody(song["melody"])
            s.melody = melody

        if "category" in song:

            category = Category.objects.filter(name__iexact=song["category"]).first()

            if not category:
                category = self._create_category(song["category"])

            s.category.set([category])

        if "composer" in song:

            composer = Writer.objects.filter(name__iexact=song["composer"]).first()

            if not composer:
                composer = self._create_writer(song["composer"])

            s.composer.set([composer])

        if "author" in song:

            if song["author"] != None:

                author = Writer.objects.filter(name__iexact=song["author"]).first()

                if not author:
                    author = self._create_writer(song["author"])

                s.author.set([author])

        s.save()
        print("created song")
        print(s)

    def handle(self, *args, **options):

        print(os.getcwd())

        backup_dir = "songs_backup/"

        files = os.listdir(os.getcwd() + "/" + backup_dir)

        for f in files:
            if f.endswith(".json"):
                j = open(backup_dir + f, "r", encoding="UTF-8").read()

                j = json.loads(j)

                for song in j:
                   self._create_song(song)
