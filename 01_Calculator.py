def calculator():
    while True:
        print("\n===== PYTHON CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5):")

        if choice == "5" :
            print("Calculator Closed. Goodbye!")
            break

        if choice not in ["1","2","3","4"]:
            print("Invalid choice! Please Select 1-5.")
            continue

        try:
            num1 = float(input("Enter first number :"))
            num2 = float(input("enter second number :"))

            if choice == "1" :
               result = num1 + num2
               operation = "+"

            elif choice == "2":
                result = num1 - num2
                operation = "-"

            elif choice == "3":
                result = num1 * num2
                operation = "*"

            elif choice == "4":
                if num2 == 0:
                    print("Error : Cannot divide by zero!")
                    continue

                result = num1 /num2
                operation = "/"

            print(f"Result : {num1} {operation} {num2} = {result}")

        except ValueError:
                print("Invalid input ! Please enter the valid numbers.")


calculator()
                
