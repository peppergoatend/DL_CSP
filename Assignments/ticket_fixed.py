# DL, Ticket Fixed

age_input = input("Enter your age: ")

# Check that the age is a whole number of 0 or more
try:
    age = int(age_input)
    if age < 0:
        print("Invalid age")
        exit()
except ValueError:
    print("Invalid age")
    exit()

matinee = input("Is this a matinee? (yes/no): ").lower()

# Determine ticket price by age
if age <= 4:
    price = 0
elif age <= 12:
    price = 8
elif age <= 64:
    price = 12
else:
    price = 9

# Apply the matinee discount without going below $0
if matinee == "yes":
    price = max(0, price - 3)

# Print the price with two decimal places
print(f"Ticket price: ${price:.2f}")
z
