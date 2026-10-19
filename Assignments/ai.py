def main():
    print("--- Personal Finance Calculator ---\n")
    
    # 1. Collect monthly income
    income = float(input("What is your monthly income: $"))
    
    # Avoid division by zero if income is 0 or negative
    if income <= 0:
        print("Income must be greater than zero.")
        return

    # 2. Collect expenses
    rent = float(input("What is your monthly rent/mortgage: $"))
    utilities = float(input("What is your monthly utilities: $"))
    groceries = float(input("What is your monthly groceries: $"))
    transportation = float(input("What is your monthly transportation: $"))

    # 3. Perform calculations
    # Standard recommendation: 10% towards savings
    savings_rate = 0.10
    savings = income * savings_rate

    # Calculate percentages of total income
    rent_pct = (rent / income) * 100
    utilities_pct = (utilities / income) * 100
    groceries_pct = (groceries / income) * 100
    transportation_pct = (transportation / income) * 100
    savings_pct = savings_rate * 100

    # Calculate remaining spending money
    total_expenses_and_savings = rent + utilities + groceries + transportation + savings
    spending_money = income - total_expenses_and_savings

    # 4. Display results
    print("\n--- Budget Summary ---")
    print(f"Your rent is ${rent:.2f} and that is {rent_pct:.0f}% of your income.")
    print(f"Your utilities are ${utilities:.2f} and that is {utilities_pct:.0f}% of your income.")
    print(f"Your groceries are ${groceries:.2f} and that is {groceries_pct:.0f}% of your income.")
    print(f"Your transportation is ${transportation:.2f} and that is {transportation_pct:.0f}% of your income.")
    print(f"You should save ${savings:.2f} a month, that is {savings_pct:.0f}% of your income.")
    print(f"You have ${spending_money:.2f} of spending money each month!")

if __name__ == "__main__":
    main()