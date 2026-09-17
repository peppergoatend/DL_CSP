# DL, Physical & Logical Memory
while True:
        name = input("Tell me your name:").strip().title()
        if name.isnumeric():
            print("Sorry, that is a number. Please enter your name.")
        else:
            break

print(f"Hello, {name}!")
