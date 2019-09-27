from dotenv import load_dotenv
import glob

import spotipy
import os

import sys
import json

load_dotenv()

# from spotipy.oauth2 import SpotifyClientCredentials

# client_credentials_manager = SpotifyClientCredentials()

totalTracks = []

files = glob.glob("*.json")
for file in files:
    myFile = open(file, "r")
    tracks = json.loads(myFile.read())
    for track in tracks:
        totalTracks.append(track["id"])
    myFile.close()

finalFile = open("tracks.json", "w")
finalFile.write(json.dumps(totalTracks))
finalFile.close()
