# DL, Your Budget Assignment
income = float(input("What is your monthly income:"))

rent = float(input("What is your monthly rent:"))

utilities = float(input("What is your monthly utilities:"))

groceries = float(input("What is your monthly groceries:"))

transportation = float(input("What is your monthly transportation:"))

print(f"Your rent is ${round (rent, 2)} and that is {round(rent/income*100)} % of your income.")
print(f"Your utilities are ${round(utilities, 2)} and that is {round(utilities/income*100)} % of your income.")
print(f"Your groceries are ${round(groceries, 2)} and that is {round(groceries/income*100)} % of your income.")
print(f"Your transportation costs are ${round(transportation, 2)} and that is {round(transportation/income*100)} % of your income.")

print(f"You should save ${round(income/10, 2)} a month, that is 10% of your income.")
print(f"You have ${round(income - (rent + utilities + groceries + transportation) - income/10, 2)} of spending money each month!")