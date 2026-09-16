def bubble_sort_4_steps(arr):
    data = list(arr)
    n = len(data)
    step_count = 1
    
    print(f"\nInitial State: {data}")
    print("-" * 45)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                left, right = data[j], data[j + 1]
                # Perform the swap
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                
                print(f"Step {step_count}: Swap {left} ↔ {right} | Current List: {data}")
                step_count += 1
                
        # If no numbers were swapped in a full pass, the list is already sorted
        if not swapped:
            break
            
    return data

# --- Run Program ---
if __name__ == "__main__":
    print("=== Interactive Bubble Sort Tracker ===")
    user_input = input("Enter numbers separated by spaces : ")
    
    try:
        numbers = [int(x) for x in user_input.split()]
        
        if not numbers:
            print("Error: Please enter some numbers.")
        else:
            final_list = bubble_sort_4_steps(numbers)
            print("-" * 45)
            print(f"Final Sorted Result: {final_list}")
            
    except ValueError:
        print("Error: Please only enter whole numbers separated by spaces.")
