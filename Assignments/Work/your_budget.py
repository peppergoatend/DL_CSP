# DL, Your Budget Assignment
income = float(input("What is your monthly income:"))

rent = float(input("What is your monthly rent:"))

utilities = float(input("What is your monthly utilities:"))

groceries = float(input("What is your monthly groceries:"))

transportation = float(input("What is your monthly transportation:"))

print(f"Your rent is ${rent} and that is {rent/income*100} % of your income.")
print(f"Your utilities are ${utilities} and that is {utilities/income*100} % of your income.")
print(f"Your groceries are ${groceries} and that is {groceries/income*100} % of your income.")
print(f"Your transportation costs are ${transportation} and that is {transportation/income*100} % of your income.")

print(f"You should save ${income/10} a month, that is 10% of your income.")
print(f"You have $ of spending money each month!")