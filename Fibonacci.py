def generate_fibonacci():
    # Loop continuously until the user enters a valid number
    while True:
        try:
            n_terms = int(input("How many Fibonacci terms would you like to see? "))
            if n_terms <= 0:
                print("❌ Please enter a positive number greater than 0.")
                continue  # Restarts the loop to ask again
            break  # Exits the loop if input is valid
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")

    # Initialize the starting terms
    n1, n2 = 0, 1
    
    print(f"\nGenerating {n_terms} terms of the Fibonacci sequence:")
    
    # Generate and print the sequence using a for loop
    for _ in range(n_terms):
        print(n1, end=" ")   # end=" " prints everything horizontally with spaces
        
        # Calculate next term and update variables simultaneously
        n1, n2 = n2, n1 + n2
    print()  # Adds a clean line break at the end

# Run the program
generate_fibonacci()
