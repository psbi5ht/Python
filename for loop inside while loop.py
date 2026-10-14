# Outer WHILE loop: Keeps the planner running indefinitely until you choose to quit
while True:
    print("\n=============================")
    print("💪 CREATE A NEW EXERCISE")
    print("\n=============================")
    
    exercise_name = input("Enter exercise name (or type 'quit' to exit): ")
    
    # Check if the user wants to close the program
    if exercise_name.lower() == 'quit':
        print("\nWorkout session finished! Great job today! 🎉")
        break  # Stops the outer while loop
        
    # Ask the user to define the exact number of iterations for the inner loop
    total_sets = int(input(f"How many sets of {exercise_name} will you do? "))
    
    print(f"\n🚀 Starting your {exercise_name} routine:")
    
    # Inner FOR loop: Runs a fixed number of times based on user input
    for set_num in range(1, total_sets + 1):
        input(f"  🏋️ Set {set_num}/{total_sets} - Press ENTER when finished...")
        print("  ✅ Set complete! Take a brief rest.")
        
    print(f"\n⭐ Awesome! You finished all {total_sets} sets of {exercise_name}!")
