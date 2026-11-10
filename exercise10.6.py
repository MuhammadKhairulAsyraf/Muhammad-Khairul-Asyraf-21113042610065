try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

except ValueError:
    print("Please enter numbers only.")

else:
    result = number1 + number2
    print(f"The sum is {result}.")