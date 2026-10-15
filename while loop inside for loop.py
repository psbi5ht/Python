# The outer FOR loop runs a fixed number of times (3 students)
for student_num in range(1, 4):
    print(f"\n=============================")
    print(f"👨‍🎓 STUDENT #{student_num}")
    print(f"=============================")
    
    student_name = input("Enter student name: ")
    scores = []
    
    # The inner WHILE loop runs indefinitely until 'done' is entered
    while True:
        score_input = input(f"  Enter test score for {student_name} (or type 'done'): ")
        
        # Check if the teacher is finished adding scores for THIS student
        if score_input.lower() == 'done':
            break  # Stops the inner while loop only
            
        # Convert the input to a number and save it
        score = float(score_input)
        scores.append(score)
        print(f"  📝 Saved score: {score}")
        
    # This code runs after the inner while loop breaks, but before the next student
    if scores:
        average = sum(scores) / len(scores)
        print(f"\n📊 {student_name}'s Average Score: {average:.2f}")
    else:
        print(f"\n⚠️ No scores entered for {student_name}.")

print("\n🎉 All 3 students have been processed! Gradebook closed.")
