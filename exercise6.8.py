pet1 = {
    'animal': 'dog',
    'owner': 'alice',
}

pet2 = {
    'animal': 'cat',
    'owner': 'budi',
}

pet3 = {
    'animal': 'rabbit',
    'owner': 'charlie',
}

pet4 = {
    'animal': 'parrot',
    'owner': 'diana',
}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print(f"\nAnimal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}")