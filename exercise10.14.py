from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)

    return None


def get_new_username(path):
    username = input("What is your name? ")

    contents = json.dumps(username)
    path.write_text(contents)

    return username


def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)

    if username:
        correct = input(f"Are you {username}? (y/n): ")

        if correct.lower() == "y":
            print(f"Welcome back, {username}!")
            return

    username = get_new_username(path)
    print(f"We'll remember you when you come back, {username}!")


greet_user()