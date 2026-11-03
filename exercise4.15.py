# Exercise 4-3: Counting to Twenty

for number in range(1, 21):
    print(number)


# Exercise 4-6: Odd Numbers

odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)


# Exercise 4-8: Cubes

cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)