from exercise11_2 import city_country

def test_city_country():
    result = city_country("Jakarta", "Indonesia")
    assert result == "Jakarta, Indonesia"


def test_city_country_population():
    result = city_country("Jakarta", "Indonesia", 10000000)
    assert result == "Jakarta, Indonesia - population 10000000"