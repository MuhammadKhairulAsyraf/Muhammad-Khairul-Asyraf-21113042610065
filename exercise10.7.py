print("Enter 'q' to quit.")

while True:
    number1 = input("Enter first number: ")

    if number1.lower() == "q":
        break

    number2 = input("Enter second number: ")

    if number2.lower() == "q":
        break

    try:
        result = int(number1) + int(number2)

    except ValueError:
        print("Please enter numbers only.")

    else:
        print(f"The sum is {result}.")