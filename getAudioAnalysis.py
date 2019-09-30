from dotenv import load_dotenv
import glob

import spotipy
import os

import sys
import json

import time

load_dotenv()

from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

i = 0

files = glob.glob("tracks/*.json")

for file in files:
    myFile = open(file, "r")
    tracks = json.loads(myFile.read())

    for track in tracks:
        results = sp.audio_analysis(track)
        f = open('audioAnalysis/'+track+'.json', 'w');
        f.write(json.dumps(results))
        f.close()

        print i, track
        i = i+1

        if i % 20 == 0:
            print i, "sleep"
            time.sleep(5)
