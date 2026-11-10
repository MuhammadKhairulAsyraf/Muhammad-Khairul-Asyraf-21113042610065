filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as file:
            contents = file.read()

    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")

    else:
        print(f"\nReading {filename}:")
        print(contents)