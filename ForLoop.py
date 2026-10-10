# 1. Ask the user how many inputs they want to provide
total_inputs = int(input("How many exam scores do you want to enter? "))

# Create an empty list to store the scores
scores_list = []

# 2. Use a for loop to run exactly that many times
# range(1, total_inputs + 1) helps display "Score 1", "Score 2", etc.
for i in range(1, total_inputs + 1):
    score = float(input(f"Enter score #{i}: "))
    scores_list.append(score)

# 3. Process the collected data outside the loop
total_sum = sum(scores_list)
average = total_sum / total_inputs

print("\n--- Results ---")
print(f"All scores entered: {scores_list}")
print(f"The average score is: {average:.2f}")
