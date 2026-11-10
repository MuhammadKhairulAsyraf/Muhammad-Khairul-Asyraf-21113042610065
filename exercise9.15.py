from random import choice

lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]

my_ticket = [1, "A", 5, "C"]

attempts = 0

while True:
    winning_items = []

    while len(winning_items) < 4:
        item = choice(lottery_items)
        if item not in winning_items:
            winning_items.append(item)

    attempts += 1

    if set(winning_items) == set(my_ticket):
        break

print(f"It took {attempts} attempts to win.")