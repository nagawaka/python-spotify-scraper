import json

totalTracks = []
totalBatch = 50

tracksFile = open("tracks.json", "r")
tracks = json.loads(tracksFile.read())
totalTracks = len(tracks)
tracksFile.close()
pages = totalTracks / totalBatch

for x in range(pages):
    file = open("tracks/tracks-"+str(x)+".json", "w")
    file.write(json.dumps(tracks[slice(x*totalBatch, totalBatch*(x+1))]))
    file.close()
