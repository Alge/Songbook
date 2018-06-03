# -*- coding: utf-8 -*-
import json

songs = json.loads(open("data.txt", "r").read())

for song in songs:
    #print(song["title"])

    data = song["data"].split("\n")

    for d in data:
        if "Melodi: " in d:
            song["melody"] = d[len("Melodi: "):]
            #print("found melody: {}".format(song["melody"]))

        elif "rfattare: " in d:
            song["writer"] = d[len("rfattare: ") + 2:]
            #print("found writer: {}".format(song["writer"]))

        elif len(d)>0:
            song["comment"] = d
            print("found data: {}".format(song["comment"]))

        try:
            d.pop('data', None)
        except:
            pass


outfile = open("out.txt", "w")

outfile.write(json.dumps(songs, ensure_ascii=False))