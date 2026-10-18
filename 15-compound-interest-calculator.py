print("=== COMPOUND INTEREST CALCULATOR ===")

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time (years): "))

if principal < 0 or rate < 0 or time < 0:
    print("Invalid input! Values cannot be negative.")

else:
    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal

    print("Principal Amount:", round(principal, 2))
    print("Compound Interest:", round(compound_interest, 2))
    print("Total Amount:", round(amount, 2))
