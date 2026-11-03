cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10600000,
        'fact': 'Jakarta is the capital city of Indonesia.',
    },

    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'Tokyo is one of the largest metropolitan areas in the world.',
    },

    'paris': {
        'country': 'france',
        'population': 2100000,
        'fact': 'Paris is famous for the Eiffel Tower.',
    },
}

for city, information in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {information['country'].title()}")
    print(f"Population: {information['population']:,}")
    print(f"Fact: {information['fact']}")