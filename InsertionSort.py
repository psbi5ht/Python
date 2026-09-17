def insertion_sort_verbose(arr):
    step_count = 1
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Check if we need to move elements
        moved = False
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            moved = True
            
        arr[j + 1] = key
        
        # Print the list after positioning the 'key' element
        if moved or i < 5:  # Shows the first few steps clearly
            print(f"Step {step_count}: Positioned {key} -> {arr}")
            step_count += 1

# 1. Ask the user for numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# 2. Convert the input string into a list of integers
numbers = [int(x) for x in user_input.split()]

print("\nOriginal array:", numbers)
print("-" * 35)

# 3. Run the step-by-step sorting
insertion_sort_verbose(numbers)
