favorite_places = {
    'alice': ['bali', 'paris', 'tokyo'],
    'budi': ['jakarta', 'bandung'],
    'charlie': ['london', 'new york', 'singapore'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")

    for place in places:
        print(f"\t{place.title()}")