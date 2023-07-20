import math

print("Welcome to the Calculator!")

while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Quit")

    choice = input("Enter your choice (1-10): ")

    if choice == '10':
        print("Calculator program exited.")
        break

    if choice == '6' or choice == '7' or choice == '8' or choice == '9':
        num = float(input("Enter the number: "))

        if choice == '6':
            print("Result: ", math.sqrt(num))
        elif choice == '7':
            print("Result: ", math.sin(num))
        elif choice == '8':
            print("Result: ", math.cos(num))
        elif choice == '9':
            print("Result: ", math.tan(num))
        else:
            print("Invalid input. Please select a valid option.")
    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result: ", num1 + num2)
        elif choice == '2':
            print("Result: ", num1 - num2)
        elif choice == '3':
            print("Result: ", num1 * num2)
        elif choice == '4':
            print("Result: ", num1 * num2)
        elif choice == '5':
            print("Result: ", num1 / num2)
        else:
            print("Invalid input. Please select a valid option.")

    print()  # Add a blank line for readability
