with open("alice.txt", "w") as file:
    file.write("The cat and the dog. The cat is cute.")

with open("alice.txt") as file:
    contents = file.read()

print("The appears:", contents.lower().count("the"), "times")