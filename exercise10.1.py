from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

print("--- Reading the entire file:")
print(contents)

print("--- Looping over each line:")
lines = contents.splitlines()

for line in lines:
    print(line)

print("--- Storing lines in a list:")
lines = contents.splitlines()

for line in lines:
    print(line)