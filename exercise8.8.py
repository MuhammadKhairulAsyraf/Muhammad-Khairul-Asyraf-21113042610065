def make_album(artist, title):
    """Build a dictionary containing album information."""
    return {
        "artist": artist.title(),
        "title": title.title(),
    }


print("Enter 'quit' at any time to stop.")

while True:
    title = input("\nWhat album are you thinking of? ")

    if title == "quit":
        break

    artist = input("Who's the artist? ")

    if artist == "quit":
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")