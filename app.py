from spotdl import Spotdl
from pathlib import Path

downloader = Spotdl(
    client_id='#client id',
    client_secret='#client secret'
)


songs_query = downloader.search(['spotify/youtube'])

for song in songs_query:
    downloader.download(song)

    