class Restaurant:
    """Membuat informasi restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")


restaurant1 = Restaurant("Mie Ayam Pak Budi", "Indonesian Food")
restaurant2 = Restaurant("Pizza Hut", "Italian Food")
restaurant3 = Restaurant("Sushi Hiro", "Japanese Food")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()