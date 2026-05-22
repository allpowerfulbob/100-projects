while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /, **, %) :")
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            result = "Error: Cannot divide by zero."
        else:
            result = num1 / num2
    elif operator == "**":
        result = num1 ** num2
    elif operator == "%":
        result = num1 % num2
    else:
        result = "Invalid operaotor"
    print("The result is: ", result)

    again = input("Calclualte again? (y/n): ").lower()
    if again != "y":
        break