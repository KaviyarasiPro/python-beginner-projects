print("=== BMI CALCULATOR ===")

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

if weight <= 0 or height <= 0:
    print("Invalid input! Weight and height must be greater than zero.")

else:
    bmi = weight / (height * height)

    print("Your BMI:", round(bmi, 2))

    if bmi < 18.5:
        print("Category: Underweight")

    elif bmi < 25:
        print("Category: Normal weight")

    elif bmi < 30:
        print("Category: Overweight")

    else:
        print("Category: Obesity")
