def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract y from x."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide x by y. Handles division by zero."""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def calculator():
    """Run a continuous command-line calculator."""
    print("=== Python Calculator ===")
    print("Select an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    while True:
        print("\n--- New Calculation ---")
        choice = input("Enter choice (1-5): ").strip()

        # Check if the user wants to exit
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        # Validate operation choice
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please choose a valid option (1-5).")
            continue

        # Get user numeric inputs with error handling
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        # Perform the selected operation
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result: {num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()
