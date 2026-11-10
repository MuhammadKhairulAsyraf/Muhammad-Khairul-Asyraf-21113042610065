from pathlib import Path
import json

user_info = {
    "username": "khairul",
    "favorite_number": 7,
    "favorite_language": "Python"
}

path = Path("user_info.json")
contents = json.dumps(user_info)
path.write_text(contents)

print("User information saved!")