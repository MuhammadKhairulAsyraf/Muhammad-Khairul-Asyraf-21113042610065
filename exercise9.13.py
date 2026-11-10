from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


print("Six-sided die:")
die = Die()
for _ in range(10):
    die.roll_die()

print("\nTen-sided die:")
die = Die(10)
for _ in range(10):
    die.roll_die()

print("\nTwenty-sided die:")
die = Die(20)
for _ in range(10):
    die.roll_die()