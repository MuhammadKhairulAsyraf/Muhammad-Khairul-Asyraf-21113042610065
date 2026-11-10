class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Battery size: {self.battery_size}-kWh")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


car = ElectricCar("Tesla", "Model S", 2025)

car.battery.describe_battery()
car.battery.upgrade_battery()
car.battery.describe_battery()