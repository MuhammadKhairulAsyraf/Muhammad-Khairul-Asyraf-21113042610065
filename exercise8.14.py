def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_info = {
        "manufacturer": manufacturer.title(),
        "model": model.title(),
    }

    for option, value in options.items():
        car_info[option] = value

    return car_info


car = make_car(
    "subaru",
    "outback",
    color="blue",
    tow_package=True
)

print(car)

another_car = make_car(
    "honda",
    "accord",
    year=2020,
    color="black"
)

print(another_car)