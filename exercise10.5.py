from pathlib import Path

path = Path("guest_book.txt")

while True:
    name = input("What's your name? (q to quit): ")

    if name.lower() == "q":
        break

    print(f"Hello, {name}!")

    with path.open("a") as file:
        file.write(f"{name}\n")