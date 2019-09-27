from dotenv import load_dotenv


import spotipy
import os

import sys
import json

load_dotenv()

from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()

def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def show_album_tracks(album):
    tracks = []
    results = sp.album_tracks(album['id'])
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    f = open(album['id'] + '.json', 'w');
    f.write(json.dumps(tracks))
    f.close()
    # for track in tracks:
    #     print('  ', track['name'])
    #     print()
    #     print(track)

def show_artist_albums(id):
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    print('Total albums:', len(albums))
    unique = set()  # skip duplicate albums
    for album in albums:
        name = album['name'].lower()
        if not name in unique:  
            # print(name)
            unique.add(name)
            show_album_tracks(album)

def show_artist(artist):
    print('====', artist['name'], '====')
    print('Popularity: ', artist['popularity'])
    if len(artist['genres']) > 0:
        print('Genres: ', ','.join(artist['genres']))

if __name__ == '__main__':
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace = False

    if len(sys.argv) < 2:
        print(('Usage: {0} artist name'.format(sys.argv[0])))
    else:
        name = ' '.join(sys.argv[1:])
        artist = get_artist(name)
        # show_artist(artist)
        show_artist_albums(artist)