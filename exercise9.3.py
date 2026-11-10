class User:
    """Menyimpan informasi pengguna."""

    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


user1 = User("Andi", "Saputra", 20, "andi@email.com", "Jakarta")
user2 = User("Budi", "Santoso", 22, "budi@email.com", "Bandung")
user3 = User("Siti", "Aminah", 21, "siti@email.com", "Surabaya")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()