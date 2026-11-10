from pathlib import Path

name = input("What's your name? ")

path = Path("guest.txt")
path.write_text(name)

print(f"Welcome, {name}!")