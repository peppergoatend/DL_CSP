# DL, Nesting
 
"""count = 2

while count <= 20:
    print(count)
    count += 2

for count in range (0.21,2):
    print(count)"""

csp = ["Remy", "Alex", "Gabe", "Bliss", "Elsie", "Evan", "Caydon", "Kaylee", "Levi", "Masen", "William", "Carrera", "Jacob", "Selena", "Ainsley", "Kristian"]

if len(csp) > 0:
    for student in csp:
        print(f"Checking in {student}")
else:
    print("There is no one in this class.")


while True:
    username = input("What is your username:").strip()
    password = input("What is your password:").strip()

    if username == "Le" and password == "password":
        print("Welcome to the program!")
        break
    else:
        print("Those credentials were incorrect.")