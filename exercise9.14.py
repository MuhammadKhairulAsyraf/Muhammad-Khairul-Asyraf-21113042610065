from random import choice

lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]

winning_items = []

while len(winning_items) < 4:
    item = choice(lottery_items)
    if item not in winning_items:
        winning_items.append(item)

print("Winning combination:", winning_items)