import glob

import json

totalTracks = []

files = glob.glob("trackInfos/*.json")

i = 0

featureFiles = glob.glob("trackAudio/*.json")

for file in files:
    myFile = open(file, "r")
    tracks = json.loads(myFile.read())
    j = 0
    for track in tracks["tracks"]:
        featureFile = open(featureFiles[i], "r")
        features = json.loads(featureFile.read())

        track["features"] = features[j]
        print track["id"], track["name"], features[j]["id"]
        
        totalTracks.append(track)

        j = j+1
        featureFile.close()

    myFile.close()
    i = i+1

finalFile = open("tracks_final.json", "w")
finalFile.write(json.dumps(totalTracks))
finalFile.close()
