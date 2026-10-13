order_number = 1

# Outer WHILE loop: Manages the entire app lifecycle
while True:
    print(f"\n=============================")
    print(f"📦 CREATING NEW ORDER #{order_number}")
    print(f"=============================")
    
    customer_name = input("Enter customer name (or type 'exit' to close app): ")
    
    # Check if the user wants to shut down the whole application
    if customer_name.lower() == 'exit':
        print("\nShutting down the system. Goodbye!")
        break # Breaks the outer loop
        
    items_ordered = []
    
    # Inner WHILE loop: Collects multiple food items for THIS specific customer
    while True:
        food_item = input(f"  Enter food item for {customer_name} (or type 'done'): ")
        
        # Check if the user is finished adding items to this specific order
        if food_item.lower() == 'done':
            break # Breaks only the inner loop
            
        items_ordered.append(food_item)
        print(f"  🛒 Added: {food_item}")

    # This code executes right after the inner loop breaks
    print(f"\n✅ Order #{order_number} Complete for {customer_name}!")
    print(f"📋 Items: {', '.join(items_ordered)}")
    
    order_number += 1  # Increment order count for the next run
