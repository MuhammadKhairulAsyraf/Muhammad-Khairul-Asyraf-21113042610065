# VERSION 1: Conditional test in the while statement

print("VERSION 1: Conditional Test")

topping = input("Enter a topping ('quit' to stop): ")

while topping != 'quit':
    print(f"I'll add {topping} to your pizza.")
    topping = input("Enter another topping ('quit' to stop): ")


# VERSION 2: Active variable

print("\nVERSION 2: Active Variable")

active = True

while active:
    topping = input("Enter a topping ('quit' to stop): ")

    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")


# VERSION 3: Break statement

print("\nVERSION 3: Break Statement")

while True:
    topping = input("Enter a topping ('quit' to stop): ")

    if topping == 'quit':
        break

    print(f"I'll add {topping} to your pizza.")

print("\nAll versions are finished!")