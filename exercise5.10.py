current_users = ['admin', 'jaden', 'john', 'alice', 'mike']

new_users = ['Jaden', 'alex', 'sarah', 'JOHN', 'david']

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is already taken. Please enter a new username.")
    else:
        print(f"{new_user} is available.")