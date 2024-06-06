def display_menu():
    print("\nSimple Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def get_numbers():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            a, b = get_numbers()
            result = add(a, b)
            print(f"Result: {a} + {b} = {result}")

        elif choice == '2':
            a, b = get_numbers()
            result = subtract(a, b)
            print(f"Result: {a} - {b} = {result}")

        elif choice == '3':
            a, b = get_numbers()
            result = multiply(a, b)
            print(f"Result: {a} * {b} = {result}")

        elif choice == '4':
            a, b = get_numbers()
            result = divide(a, b)
            print(f"Result: {a} / {b} = {result}")

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
