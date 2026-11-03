favorite_numbers = {
    'alice': [7, 12, 21],
    'budi': [10, 5],
    'charlie': [3, 9, 15],
    'diana': [8, 16],
    'eric': [4, 11, 20],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")

    for number in numbers:
        print(number)