def make_album(artist, title, num_songs=None):
    """Build a dictionary containing information about an album."""
    album = {
        "artist": artist.title(),
        "title": title.title(),
    }

    if num_songs is not None:
        album["num_songs"] = num_songs

    return album


print(make_album("metallica", "ride the lightning"))
print(make_album("beethoven", "ninth symphony"))
print(make_album("willie nelson", "red-headed stranger"))
print(make_album("iron maiden", "piece of mind", num_songs=8))