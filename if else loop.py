# A program that loops until a secure password is created

while True:
    # 1. Take user input
    password = input("Create a password (must be at least 6 characters long): ")
    
    # 2. Check the condition using if-else
    if len(password) >= 6:
        print("✅ Password accepted and saved successfully!")
        break  # Stops the loop because the input is valid
    else:
        print("❌ Error: Password is too short. Please try again.\n")
