print("=== CURRENCY CONVERTER ===")

rates = {
    "INR": 1.0,
    "USD": 83.0,
    "EUR": 90.0,
    "GBP": 105.0
}

print("Available currencies: INR, USD, EUR, GBP")

from_currency = input("Convert from: ").upper()
to_currency = input("Convert to: ").upper()
amount = float(input("Enter amount: "))

if from_currency not in rates or to_currency not in rates:
    print("Invalid currency!")

elif amount < 0:
    print("Amount cannot be negative!")

else:
    amount_in_inr = amount * rates[from_currency]
    result = amount_in_inr / rates[to_currency]

    print(
        f"{amount:.2f} {from_currency} = "
        f"{result:.2f} {to_currency}"
    )
