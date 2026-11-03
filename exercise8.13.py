def build_profile(first, last, **user_info):
    """Build a dictionary containing information about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last

    return user_info


user_profile = build_profile(
    "khairul",
    "ahmad",
    age=20,
    city="jakarta",
    hobby="programming"
)

print(user_profile)