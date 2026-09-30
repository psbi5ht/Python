def check_armstrong_with_breakdown(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    print(f"\n🔢 Analyzing: {number}")
    print(f"   • Total number of digits (n) = {num_digits}")
    
    # Generate the breakdown steps
    breakdown_terms = []
    digit_sum = 0
    
    for digit in num_str:
        d_int = int(digit)
        power_val = d_int ** num_digits
        digit_sum += power_val
        breakdown_terms.append(f"{d_int}^{num_digits} ({power_val})")
    
    # Print the full math equation
    equation = " + ".join(breakdown_terms)
    print(f"   • Math: {equation} = {digit_sum}")
    
    # Final comparison
    if digit_sum == number:
        print(f"✨ Result: {digit_sum} == {number} -> It is an Armstrong number!\n")
        return True
    else:
        print(f"❌ Result: {digit_sum} != {number} -> It is NOT an Armstrong number.\n")
        return False

def main():
    print("--- Armstrong Checker with Math Breakdown ---")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("Enter a number to check: ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        if not user_input.isdigit():
            print("❌ Invalid input! Enter a positive integer.\n")
            continue
            
        check_armstrong_with_breakdown(int(user_input))
        print("-" * 45)

if __name__ == "__main__":
    main()
