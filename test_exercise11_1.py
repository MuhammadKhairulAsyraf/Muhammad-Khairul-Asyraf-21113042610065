from exercise11_1 import city_country

def test_city_country():
    result = city_country("Jakarta", "Indonesia")
    assert result == "Jakarta, Indonesia"