def display_message():
    """Tampilkan pesan tentang materi yang sedang dipelajari."""
    print("I am learning about functions in Python.")


def favorite_book(title):
    """Tampilkan judul buku favorit."""
    print(f"One of my favorite books is {title}.")


def describe_city(city, country="Indonesia"):
    """Tampilkan nama kota dan negaranya."""
    print(f"{city} is in {country}.")


# Memanggil ketiga fungsi
display_message()

favorite_book("Python Crash Course")

describe_city("Jakarta")
describe_city("Tokyo", "Japan")