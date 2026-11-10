from random import randint
from datetime import date

today = date.today()

print("Today's date:", today)
print("Random number:", randint(1, 100))
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)