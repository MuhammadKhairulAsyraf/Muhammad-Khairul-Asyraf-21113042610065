foods = ('rice', 'chicken', 'fish', 'soup', 'salad')

print("Original menu:")
for food in foods:
    print(food)

# Trying to change one item
foods[0] = 'noodles'

# Changing the restaurant menu
foods = ('noodles', 'beef', 'fish', 'soup', 'salad')

print("\nRevised menu:")
for food in foods:
    print(food)