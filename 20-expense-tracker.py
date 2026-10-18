print("=== EXPENSE TRACKER ===")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")

        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Amount must be greater than zero!")
            else:
                expense = {
                    "name": name,
                    "amount": amount
                }

                expenses.append(expense)
                print("Expense added successfully!")

        except ValueError:
            print("Invalid amount! Please enter a number.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")

        else:
            print("\n--- YOUR EXPENSES ---")

            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. {expense['name']} - "
                    f"₹{expense['amount']:.2f}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)

        print(f"Total Expenses: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please select 1-4.")
