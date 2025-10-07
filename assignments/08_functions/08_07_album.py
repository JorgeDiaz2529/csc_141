def make_album(artist: str, title: str, song_count: int=None):
    album = {'artist': artist, 'title': title}
    if song_count:
        album['song_count'] = song_count

    return album
# This file creates an album dictionary

albums = []
albums.append(make_album("John Ham", "The Hammers"))
albums.append(make_album("Malk Tans", "Malker Time"))
albums.append(make_album("Liam", "200 Liams", 10))

for album in albums:
    print(album)