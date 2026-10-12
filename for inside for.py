# Ask how many students are in the class (Controls the Outer Loop)
num_students = int(input("How many students do you want to grade? "))

# Ask how many subjects each student takes (Controls the Inner Loop)
num_subjects = int(input("How many subjects does each student have? "))

# Outer FOR loop: Iterates through each student
for student_num in range(1, num_students + 1):
    print(f"\n--- Entering Data for Student #{student_num} ---")
    
    student_name = input("Enter student name: ")
    total_marks = 0
    
    # Inner FOR loop: Runs completely from scratch for every single student
    for subject_num in range(1, num_subjects + 1):
        marks = float(input(f"  Enter marks for Subject {subject_num}: "))
        total_marks += marks  # Add marks together
        
    # Calculate average after the inner loop finishes for this student
    average = total_marks / num_subjects
    print(f"📊 {student_name}'s Average Score: {average:.2f}")

print("\nAll student data has been processed successfully!")
