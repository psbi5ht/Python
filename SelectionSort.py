def selection_sort_with_swap_details(arr):
    n = len(arr)
    step = 1
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Capture the values before swapping them
        val_at_i = arr[i]
        val_at_min = arr[min_idx]
        
        # Swap the elements
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Display the step, the array state, and details about the swap
        if min_idx != i:
            print(f"Step {step}: {arr}  -> (Swapped {val_at_i} and {val_at_min})")
        else:
            print(f"Step {step}: {arr}  -> ({val_at_i} is already in the correct position)")
            
        step += 1

# --- User Input Section ---
try:
    user_input = input("Enter your numbers separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]
    
    if len(numbers) == 0:
        print("You didn't enter any numbers!")
    else:
        print(f"\nInitial Array: {numbers}")
        print("-" * 65)

        # Run the tracking sort
        selection_sort_with_swap_details(numbers)

        print("-" * 65)
        print(f"Final Sorted Result: {numbers}")

except ValueError:
    print("Error: Please enter numbers only (separated by spaces).")
