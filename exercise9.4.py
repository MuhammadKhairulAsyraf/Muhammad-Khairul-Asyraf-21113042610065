class Restaurant:
    """Membuat informasi restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("Mie Ayam Pak Budi", "Indonesian Food")

print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 10
print(f"Customers served: {restaurant.number_served}")

restaurant.set_number_served(25)
print(f"Customers served: {restaurant.number_served}")

restaurant.increment_number_served(5)
print(f"Customers served: {restaurant.number_served}")