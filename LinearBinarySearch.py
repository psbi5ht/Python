def linear_search(arr, target):
    """Scans the list sequentially to find the target."""
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


def binary_search(arr, target):
    """Searches a sorted list by repeatedly halving the search space."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


# --- Main Program Execution ---
if __name__ == "__main__":
    print("--- Search Algorithm Simulator ---")
    
    # 1. Take list input from the user
    user_input = input("Enter numbers separated by spaces: ")
    # Convert the space-separated string into a list of integers
    numbers = [int(x) for x in user_input.split()]
    
    # 2. Take the target value input
    target = int(input("Enter the number you want to search for: "))
    
    print("\n" + "="*30)
    print(f"Original List: {numbers}")
    print(f"Target Value:  {target}")
    print("="*30 + "\n")
    
    # 3. Perform Linear Search (Works on unsorted data)
    linear_result = linear_search(numbers, target)
    if linear_result != -1:
        print(f"[Linear Search] Found! Target is at index: {linear_result}")
    else:
        print("[Linear Search] Target not found in the list.")
        
    # 4. Perform Binary Search (Requires data to be sorted)
    # We create a sorted copy so we don't mess up the original list's indices
    sorted_numbers = sorted(numbers)
    print(f"\n[Binary Search] Sorting list for binary search... New order: {sorted_numbers}")
    
    binary_result = binary_search(sorted_numbers, target)
    if binary_result != -1:
        print(f"[Binary Search] Found! Target is at index: {binary_result} (in the SORTED list)")
    else:
        print("[Binary Search] Target not found in the sorted list.")
