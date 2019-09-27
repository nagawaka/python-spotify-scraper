import glob

import json

totalTracks = []

files = glob.glob("albums/*.json")
for file in files:
    myFile = open(file, "r")
    tracks = json.loads(myFile.read())
    for track in tracks:
        totalTracks.append(track["id"])
    myFile.close()

finalFile = open("tracks.json", "w")
finalFile.write(json.dumps(totalTracks))
finalFile.close()
