# Tests for equality and inequality with strings

car = 'subaru'

print(car == 'subaru')
print(car != 'audi')


# Tests using the lower() method

name = 'Khairul'

print(name.lower() == 'khairul')
print(name.lower() == 'KHAIRUL')


# Numerical tests

age = 20

print(age == 20)
print(age != 20)
print(age > 18)
print(age < 18)
print(age >= 20)
print(age <= 18)


# Tests using and and or keywords

print(age > 18 and age < 30)
print(age > 30 and age < 40)

print(age < 18 or age == 20)
print(age > 30 or age < 10)


# Test whether an item is in a list

foods = ['pizza', 'burger', 'sushi']

print('pizza' in foods)
print('rice' in foods)


# Test whether an item is not in a list

print('rice' not in foods)
print('burger' not in foods)