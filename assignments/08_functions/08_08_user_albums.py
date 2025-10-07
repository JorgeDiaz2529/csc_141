def make_album(artist: str, title: str, song_count: int=None):
    album = {'artist': artist, 'title': title}
    if song_count:
        album['song_count'] = song_count

    return album

albums = []

while True:
    print("Make an album!")
    print("Enter 'q' at anytime to quit.")

    artist = input("Please input the artist's name: ")
    if artist == "q":
        break

    title = input("Please input the album title: ")
    if title == "q":
        break

    song_count = input("(optional) How many songs are in your album? Otherwise, type 'n': ")
    if song_count == 'q':
        break
    elif not song_count.isdigit and song_count != "n":
        print("Please input a number...")
        continue
    
    if song_count == "n":
        albums.append(make_album(artist, title))
    else:
        albums.append(make_album(artist, title, int(song_count)))

print()

for album in albums:
    print(album)