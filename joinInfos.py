import glob

import json

totalTracks = []

files = glob.glob("trackInfos/*.json")
for file in files:
    myFile = open(file, "r")
    tracks = json.loads(myFile.read())
    for track in tracks["tracks"]:
        print track["id"], track["name"]
        totalTracks.append(track)
    myFile.close()

finalFile = open("tracks_final.json", "w")
finalFile.write(json.dumps(totalTracks))
finalFile.close()
