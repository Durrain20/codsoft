def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

print("Welcome to the Simple Calculator!")

while True:
    print("\nPlease select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice in ('1', '2', '3', '4'):
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", add(number1, number2))
        elif choice == '2':
            print("Result:", subtract(number1, number2))
        elif choice == '3':
            print("Result:", multiply(number1, number2))
        elif choice == '4':
            print("Result:", divide(number1, number2))
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4/5).")
