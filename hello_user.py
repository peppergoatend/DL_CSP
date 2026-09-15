# DL, Physical & Logical Memory
while True:
        name = input("Tell me your name:").strip().capitalize()
        if name.isnumeric():
            print("Sorry, that is a number. Please enter your name.")
        elif " " in name:
            print("I said your name!")
        else:
            break

print(f"Hello, {name}!")