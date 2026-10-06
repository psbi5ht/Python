# ==========================================
# PYTHON DICTIONARY OPERATIONS PROGRAM
# ==========================================

print("--- 1. WRITE & CREATE DICTIONARY 1 ---")
num_items1 = int(input("How many items for Dictionary 1? "))
dict_one = {}
for _ in range(num_items1):
    key = input("Enter key: ")
    val_input = input(f"Enter value for '{key}': ")
    val = int(val_input) if val_input.isdigit() else val_input
    dict_one[key] = val
print(f"Dictionary 1: {dict_one}\n")


print("--- 2. EXTRACT UNIQUE DICTIONARY VALUES ---")
# Extracts unique values specifically from Dictionary 1
unique_values = {val for val in dict_one.values()}
print(f"Unique values in Dictionary 1: {unique_values}\n")


print("--- 3. FIND THE SUM OF ALL ITEMS (NUMERIC VALUES) IN A DICTIONARY ---")
# Calculates the sum of numeric values in Dictionary 1
numeric_sum = sum(val for val in dict_one.values() if isinstance(val, (int, float)))
print(f"Sum of all numeric values in Dictionary 1: {numeric_sum}\n")


print("--- 4. WRITE DICTIONARY 2 & MERGE ---")
num_items2 = int(input("How many items for Dictionary 2? "))
dict_two = {}
for _ in range(num_items2):
    key = input("Enter key: ")
    val_input = input(f"Enter value for '{key}': ")
    val = int(val_input) if val_input.isdigit() else val_input
    dict_two[key] = val
print(f"Dictionary 2: {dict_two}")

# Merging both user-inputted dictionaries using the | operator
merged_dict = dict_one | dict_two
print(f"Merged Dictionary: {merged_dict}\n")
print("Note: If you entered matching keys in both dictionaries, Dictionary 2's values overwrote Dictionary 1's values.")


print("--- 5. REMOVE ALL DUPLICATE WORDS FROM A GIVEN SENTENCE ---")
sentence_input = input("Enter a sentence with duplicate words: ")
words = sentence_input.split()
unique_words_dict = dict.fromkeys(words)
clean_sentence = " ".join(unique_words_dict.keys())
print(f"Sentence after removing duplicates: '{clean_sentence}'\n")


print("--- 6. DICTIONARY TO FIND MIRROR CHARACTERS IN A STRING ---")
mirror_str = input("Enter a string to mirror (e.g., 'abc'): ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
mirror_dict = dict(zip(alphabet, reversed(alphabet)))
mirrored_result = "".join(mirror_dict.get(char, char) for char in mirror_str.lower())
print(f"Mirrored String: {mirrored_result}\n")


print("--- 7. FIND ORDERED WORDS IN A DICTIONARY ---")
word_to_check = input("Enter a word to check if it's ordered: ")
is_ordered = list(word_to_check) == sorted(word_to_check)
print(f"Is '{word_to_check}' an ordered word?: {is_ordered}\n")


print("--- 8. WAYS TO REMOVE A KEY FROM A DICTIONARY ---")
if dict_one:
    key_to_remove = input(f"Choose a key from Dictionary 1 {list(dict_one.keys())} to remove: ")
    
    if key_to_remove in dict_one:
        dict_copy1 = dict_one.copy()
        dict_copy2 = dict_one.copy()
        
        # Method A: .pop()
        removed_val = dict_copy1.pop(key_to_remove)
        print(f"Method A (.pop()): Removed '{key_to_remove}' (value was {removed_val}). New dict: {dict_copy1}")
        
        # Method B: del statement
        del dict_copy2[key_to_remove]
        print(f"Method B (del statement): Removed '{key_to_remove}'. New dict: {dict_copy2}")
    else:
        print("Key not found in Dictionary 1.")
else:
    print("Dictionary 1 is empty, skipping key removal demonstration.")

print("\n--- PROGRAM COMPLETE ---")
