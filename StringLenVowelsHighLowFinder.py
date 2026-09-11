from collections import Counter

# 1. Get input from the user
text = input("Enter a string to analyze: ")

# Calculate the total length (including spaces and punctuation)
total_length = len(text)

# 2. Count the vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)

# 3. Find highest and lowest occurring letters
# Filter to keep only alphabetic letters and convert to lowercase for accurate counting
letters_only = [char.lower() for char in text if char.isalpha()]

if letters_only:
    # Counter counts the frequency of each letter automatically
    letter_counts = Counter(letters_only)
    
    # Find highest and lowest occurrences
    highest_letter, highest_count = letter_counts.most_common(1)[0]
    
    # Find the least common letter
    lowest_letter, lowest_count = letter_counts.most_common()[-1]
else:
    highest_letter, highest_count = "None", 0
    lowest_letter, lowest_count = "None", 0

# 4. Display the results
print("\n--- String Analysis Results ---")
print(f"Total length of the string: {total_length}")
print(f"Number of vowels: {vowel_count}")

if letters_only:
    print(f"Highest occurring letter: '{highest_letter}' (appears {highest_count} time(s))")
    print(f"Lowest occurring letter: '{lowest_letter}' (appears {lowest_count} time(s))")
else:
    print("No alphabetic letters were found to calculate frequencies.")
