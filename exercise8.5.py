def describe_city(city, country="Indonesia"):
    """Describe a city and its country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city("Jakarta")
describe_city("Bandung")
describe_city("Tokyo", "Japan")