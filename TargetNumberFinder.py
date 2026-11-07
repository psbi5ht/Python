import itertools

def solve_target(target):
    # Try using 1 digit up to 4 digits to find the shortest/simplest formula
    for r in range(1, 5):
        # Generate all combinations of digits 0-9 of length r
        for digits in itertools.product(range(10), repeat=r):
            # Generate all combinations of operators (+, -, *, /) of length r-1
            for ops in itertools.product(['+', '-', '*', '/'], repeat=r-1):
                # Build the expression sequentially (left-to-right evaluation)
                expr = str(digits[0])
                current_val = digits[0]
                valid = True
                
                for i in range(r - 1):
                    op = ops[i]
                    next_digit = digits[i + 1]
                    
                    # Avoid division by zero
                    if op == '/' and next_digit == 0:
                        valid = False
                        break
                        
                    # Calculate step-by-step
                    if op == '+': current_val += next_digit
                    elif op == '-': current_val -= next_digit
                    elif op == '*': current_val *= next_digit
                    elif op == '/': current_val /= next_digit
                    
                    expr = f"({expr} {op} {next_digit})"
                
                # Check if we hit the target exactly
                if valid and abs(current_val - target) < 1e-6:
                    return f"{expr} = {target}"
                    
    return "No simple combination found using digits 0-9."

# User Input
try:
    user_target = float(input("Enter the target number you want to make: "))
    
    # Clean up display if it's a whole number
    if user_target.is_integer():
        user_target = int(user_target)
        
    print("\nCalculating formula...")
    result = solve_target(user_target)
    print(f"Result: {result}")
    
except ValueError:
    print("Invalid input. Please enter a valid number.")
