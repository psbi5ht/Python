# Create an empty list
numbers = []

# Ask the user how many numbers they want to add
total_numbers = int(input("How many numbers do you want to enter? "))

# Loop to get each number individually
for i in range(total_numbers):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)  # This directly inserts the number into the list

# Process the list
largest = max(numbers)
smallest = min(numbers)
total_sum = largest + smallest

# --- Display Section ---
print(f"\n1. All inserted numbers: {numbers}")
print(f"2. Largest number: {largest}")
print(f"3. Smallest number: {smallest}")
print(f"4. Their sum ({largest} + {smallest}): {total_sum}")
