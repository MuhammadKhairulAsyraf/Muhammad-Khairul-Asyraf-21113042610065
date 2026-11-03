favorite_places = {
    'alice': {
        'places': ['bali', 'paris', 'tokyo'],
        'category': 'travel',
        'reason': 'She enjoys exploring new cultures.',
    },

    'budi': {
        'places': ['jakarta', 'bandung'],
        'category': 'food and travel',
        'reason': 'He enjoys local food and beautiful scenery.',
    },

    'charlie': {
        'places': ['london', 'new york', 'singapore'],
        'category': 'city life',
        'reason': 'He likes modern and busy cities.',
    },
}

for name, information in favorite_places.items():
    print(f"\nName: {name.title()}")
    print(f"Favorite category: {information['category'].title()}")
    print(f"Reason: {information['reason']}")

    print("Favorite places:")

    for place in information['places']:
        print(f"\t- {place.title()}")