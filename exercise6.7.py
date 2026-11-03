person1 = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
}

person2 = {
    'first_name': 'alice',
    'last_name': 'johnson',
    'age': 25,
    'city': 'new york',
}

person3 = {
    'first_name': 'budi',
    'last_name': 'santoso',
    'age': 30,
    'city': 'jakarta',
}

people = [person1, person2, person3]

for person in people:
    print(f"\nFirst name: {person['first_name'].title()}")
    print(f"Last name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")