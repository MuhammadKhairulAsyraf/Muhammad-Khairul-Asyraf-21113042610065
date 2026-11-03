prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

print("Thank you for using our ticket service!")