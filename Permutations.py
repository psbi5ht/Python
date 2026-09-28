from itertools import permutations

# 1. Take text input from the user
user_input = input("Enter a string to permute: ")

# 2. Generate the permutations (removes duplicates by using a set)
# We use "".join(p) to turn the tuple back into a clean string
unique_perms = sorted(list(set("".join(p) for p in permutations(user_input))))

# 3. Print the results
print(f"\nThere are {len(unique_perms)} unique permutations for '{user_input}':")
for perm in unique_perms:
    print(perm)
