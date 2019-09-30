from dotenv import load_dotenv
import glob

import spotipy
import os

import sys
import json

load_dotenv()

totalTracks = []

files = glob.glob("tracks/*.json")
separator = ","

from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

i = 0

for file in files:
    myFile = open(file, "r")
    tracks = json.loads(myFile.read())
    myTracks = separator.join(tracks)
    # print len(tracks)
    myFile.close()

    results = sp.audio_features(tracks)
    f = open('trackAudio/'+ str(i) + '.json', 'w');
    f.write(json.dumps(results))
    f.close()
    i = i+1

    print i
    print myTracks
