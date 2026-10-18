print("=== SIMPLE INTEREST CALCULATOR ===")

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time (years): "))

if principal < 0 or rate < 0 or time < 0:
    print("Invalid input! Values cannot be negative.")

else:
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    print("Principal Amount:", round(principal, 2))
    print("Simple Interest:", round(simple_interest, 2))
    print("Total Amount:", round(total_amount, 2))
