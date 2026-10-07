print("--- 1. CREATE A TUPLE ---")
user_input = input("Enter comma-separated numbers for your tuple: ")
my_tuple = tuple(int(x.strip()) for x in user_input.split(",") if x.strip())
print(f"Created Tuple: {my_tuple}\n")


print("--- 2. FIND THE SIZE ---")
print(f"Size of the tuple (Number of elements): {len(my_tuple)}\n")


print("--- 3. MAXIMUM AND MINIMUM ELEMENTS IN TUPLE ---")
print(f"Maximum Element: {max(my_tuple)}")
print(f"Minimum Element: {min(my_tuple)}\n")


print("--- 4. EXTRACT DIGITS FROM TUPLE LIST ---")
tuple_list_input = input("Enter space-separated number groups, separating tuples with commas: ")
digit_tuple_list = [
    tuple(int(num) for num in group.split()) 
    for group in tuple_list_input.split(",") if group.strip()
]
print(f"Generated List of Tuples: {digit_tuple_list}")

extracted_digits = {int(digit) for tpl in digit_tuple_list for num in tpl for digit in str(num)}
print(f"Extracted Unique Digits: {sorted(list(extracted_digits))}\n")


print("--- 5. REMOVE TUPLES OF LENGTH K (USER INPUT) ---")
# 1. Take custom list of tuples from the user
user_tuples_input = input("Enter your custom list of tuples: ")
custom_tuple_list = [
    tuple(int(num) for num in group.split()) 
    for group in user_tuples_input.split(",") if group.strip()
]
print(f"Your List of Tuples: {custom_tuple_list}")

# 2. Get length K to filter out
length_k = int(input("Enter tuple length 'K' to remove: "))

# 3. Filter and remove tuples matching length K
filtered_list = [tpl for tpl in custom_tuple_list if len(tpl) != length_k]
print(f"Filtered List (Removed length {length_k}): {filtered_list}\n")

print("--- PROGRAM FINISHED ---")
