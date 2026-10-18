
from datetime import date

print("=== AGE CALCULATOR ===")

day = int(input("Enter birth day: "))
month = int(input("Enter birth month: "))
year = int(input("Enter birth year: "))

try:
    birth_date = date(year, month, day)
    today = date.today()

    if birth_date > today:
        print("Invalid date! Birth date cannot be in the future.")

    else:
        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        print("Your age is:", age, "years")

except ValueError:
    print("Invalid date! Please enter a valid date of birth.")

