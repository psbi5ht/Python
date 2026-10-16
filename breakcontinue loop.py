print("=========================================")
print("🌡️ SMART VENT MONITORING ACTIVE")
print("=========================================")
print("Instructions:")
print("- Enter temperatures between 0°C and 50°C.")
print("- Enter a value over 100°C for emergency shutdown.")
print("- Type '-1' to exit standard operations.")
print("=========================================\n")

while True:
    user_input = input("Enter current sensor temperature (°C): ")
    
    # 1. Standard Exit Check
    if user_input == '-1':
        print("\n👋 System shut down normally by operator.")
        break  # Exits the loop entirely
        
    # Convert input to a float for numerical checking
    temp = float(user_input)
    
    # 2. EMERGENCY SHUTDOWN TRIGGER (Demonstrating BREAK)
    if temp >= 100.0:
        print(f"\n🚨 CRITICAL ERROR: Extreme heat detected ({temp}°C)!")
        print("💥 Emergency override initiated. System locked down.")
        break  # Instantly terminates the loop for safety
        
    # 3. INVALID INPUT FILTER (Demonstrating CONTINUE)
    if temp < 0.0 or temp > 50.0:
        print("⚠️ Warning: Out-of-bounds reading. Skipping processing...")
        continue  # Jumps straight back to the top of the loop for the next input
        
    # 4. Standard Processing (Only reached if both conditions above are false)
    print(f"✅ Reading stable. Adjusting vent airflow for {temp}°C.")
